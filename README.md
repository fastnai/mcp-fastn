# Fastn Server

The Fastn server is a powerful, scalable platform that enables dynamic tool registration and execution based on API definitions. It seamlessly integrates with services like Claude.ai and Cursor.ai, providing a unified server solution for a wide range of tasks. With its robust architecture, Fastn delivers exceptional performance and flexibility for real-time, API-driven operations.

## Features

- Platform-specific handling for Claude and Cursor
- **Integrated platform support** - Use services like Slack, Notion, HubSpot, and many more through the Fastn server after completing the simple setup
- Logging support

## Step-by-Step Setup Guide

### Step 1: Fastn Setup

1. Login to your Fastn account
2. Go to "Connectors" from the left sidebar
3. Activate the service(s) you want to use by clicking on activate.
4. Go to "Settings" from the left sidebar
5. Click on "Generate API Key" and save it somewhere locally (e.g., in a notepad)
6. Click on the copy button that exists on the top bar (left side of your profile)
7. Copy your Workspace ID and save it as well
8. All setup from Fastn is now complete

### Step 2: Server Setup

## Prerequisites

- Python 3.10 or higher

## Quick Start

### macOS

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# Install UV, create virtual environment, and install dependencies in one go
curl -LsSf https://astral.sh/uv/install.sh | sh && uv venv && source .venv/bin/activate && uv pip install -e .

# Run server (specify platform with --platform flag)
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID 
```

### Windows

### Windows

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# Install UV, create a virtual environment, and install dependencies
# Option 1: Install UV using pip
python -m pip install uv
# Make sure to copy the installation path and add it to your Windows environment variables.

# Option 2: Install UV using PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" && uv venv && .venv\Scripts\activate && uv pip install -e .

# Run server (specify platform with --platform flag)
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID 
```

## Step 3: Integration with Claude

1. Open the Claude configuration file:
```bash
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. Add the following configuration (replace placeholders with your actual values):
```json
{
    "mcpServers": {
        "fastn": {
            "command": "/path/to/your/uv",
            "args": [
                "--directory",
                "/path/to/your/fastn-server",
                "run",
                "fastn-server.py",
                "--api_key",
                "YOUR_API_KEY",
                "--space_id",
                "YOUR_WORKSPACE_ID"
            ]
        }
    }
}
```

## Step 4: Integration with Cursor

1. Open Cursor settings
2. Click on "MCP" in the settings menu
3. Click on "Add New"
4. Add a name for your server (e.g., "fastn")
5. Select "Command" as the type
6. Add the following command (replace placeholders with your actual values):
```
/path/to/your/uv --directory /path/to/your/fastn-server run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_WORKSPACE_ID
```

## Troubleshooting

### Package Structure Error

If you encounter an error like this during installation:
```
ValueError: Unable to determine which files to ship inside the wheel using the following heuristics:
The most likely cause of this is that there is no directory that matches the name of your project (fastn).
```

**Quick Fix:**
1. Make sure `pyproject.toml` has the wheel configuration:
```toml
[tool.hatch.build.targets.wheel]
packages = ["."]
```

2. Then install dependencies:
```bash
uv pip install "httpx>=0.28.1" "mcp[cli]>=1.2.0"
```

3. Run the server:
```bash
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID
```

## Configuration

You'll need the following credentials to run the server:

- API Key from Fastn (obtained in Step 1)
- Space ID from your Fastn workspace (obtained in Step 1)
- Platform specification (claude or cursor)

Optional: You can also specify a use case:
```bash
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID
```

## Project Structure

- `fastn-server.py` - Unified server implementation for both Claude.ai and Cursor.ai
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Dependency lock file
- `.python-version` - Python version specification


## Error Handling

The server includes comprehensive error handling for:
- HTTP requests
- Tool registration
- Parameter validation
- Tool execution
- Platform-specific requirements

## Logging

Logs are output with timestamp, level, and message in the following format:
```
%(asctime)s - %(levelname)s - %(message)s
```

## Dependencies

- httpx: HTTP client
- mcp[cli]: MCP server implementation
- pydantic: Data validation
