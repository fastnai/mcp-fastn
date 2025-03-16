from typing import Any, Dict, Tuple
import httpx
import asyncio
import json
import logging
import argparse
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, create_model

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Run MCP server with specified API credentials and use case.")
parser.add_argument("--api_key", required=True, help="API key for authentication.")
parser.add_argument("--space_id", required=True, help="Space ID for the target environment.")
parser.add_argument("--usecase", required=False, help="Description of the use case.")
args = parser.parse_args()

# Initialize FastMCP server
mcp = FastMCP("fastn")

# API Endpoints
GET_TOOLS_URL = "https://live.fastn.ai/api/v1/getTools"
EXECUTE_TOOL_URL = "https://live.fastn.ai/api/v1/executeTool"

# Common headers
HEADERS = {
    "x-fastn-api-key": args.api_key,
    "Content-Type": "application/json",
    "x-fastn-space-id": args.space_id,
    "x-fastn-space-tenantid": "",
    "stage": "LIVE"
}

async def fetch_tools() -> list:
    """Fetch tool definitions from the getTools API endpoint."""
    data = {
        "input": {
            "useCase": args.usecase,
            "spaceId" : args.space_id
        }
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(GET_TOOLS_URL, headers=HEADERS, json=data)
            response.raise_for_status()
            tools = response.json()
            logging.info(f"Fetched {len(tools)} tools.")
            return tools
        except httpx.HTTPStatusError as e:
            logging.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            logging.error(f"Request error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
    return []

async def execute_tool(action_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a tool by calling the executeTool API."""
    data = {"input": {"actionId": action_id, "parameters": parameters}}
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(EXECUTE_TOOL_URL, headers=HEADERS, json=data)
            response.raise_for_status()
            result = response.json()
            return json.dumps(result)
        except httpx.HTTPStatusError as e:
            logging.error(f"Execution failed: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            logging.error(f"Unexpected execution error: {e}")
    return {}

def build_field(param_name: str, param_schema: Dict[str, Any]) -> Tuple[Any, Any]:
    """Recursively build a Pydantic field from a JSON schema definition."""
    param_type = param_schema.get("type", "string")
    
    if param_type == "string":
        return (str, ...)
    elif param_type == "number":
        return (float, ...)
    elif param_type == "integer":
        return (int, ...)
    elif param_type == "array":
        # You could further improve this by checking the item type
        return (list, ...)
    elif param_type == "object":
        properties = param_schema.get("properties", {})
        fields = {}
        for sub_name, sub_schema in properties.items():
            fields[sub_name] = build_field(sub_name, sub_schema)
        # Create a nested Pydantic model for the object
        nested_model = create_model(f"{param_name}_model", **fields)
        return (nested_model, ...)
    else:
        return (str, ...)

def register_tool(tool_def: Dict[str, Any]):
    """Dynamically create and register a tool based on the tool definition."""
    try:
        action_id = tool_def["actionId"]
        function_info = tool_def["function"]
        function_name = function_info["name"]
        parameters_schema = function_info.get("parameters", {})
        description = function_info.get("description", "")

        # Dynamically create Pydantic model for parameters
        if parameters_schema:
            properties = parameters_schema.get("properties", {})
            fields = {}
            for param_name, param_schema in properties.items():
                fields[param_name] = build_field(param_name, param_schema)
            ParametersModel = create_model(f"{function_name}Parameters", **fields)
        else:
            ParametersModel = BaseModel

        async def dynamic_tool(params: ParametersModel):
            """Dynamically created tool function."""
            return await execute_tool(action_id, params.dict())

        # Register the tool with MCP
        dynamic_tool.__name__ = function_name
        mcp.tool(name=function_name, description=description)(dynamic_tool)

        logging.info(f"Registered tool: {function_name}")
        logging.info(f"Description: {description}")
        logging.info(f"Parameters: {json.dumps(parameters_schema, indent=2)}")
    except KeyError as e:
        logging.error(f"Invalid tool definition missing key: {e}")
    except Exception as e:
        logging.error(f"Error registering tool: {e}")

def initialize_tools():
    """Fetch tools and register them before running MCP."""
    tools_data = asyncio.run(fetch_tools())
    for tool_def in tools_data:
        register_tool(tool_def)

if __name__ == "__main__":
    initialize_tools()
    mcp.run(transport='stdio')