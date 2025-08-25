[![MseeP.ai Security Assessment Badge](https://mseep.net/mseep-audited.png)](https://mseep.ai/app/fastnai-mcp-fastn)

# Fastn Server

The Fastn server is a powerful, scalable platform that enables dynamic tool registration and execution based on API definitions. It seamlessly integrates with services like Claude.ai and Cursor.ai, providing a unified server solution for a wide range of tasks.

## Features

- **Integrated platform support** - Use services like Slack, Notion, HubSpot, and more through the Fastn server
- **Flexible authentication** - Use either API key or tenant-based authentication
- **Comprehensive logging** - Detailed logs for troubleshooting
- **Error handling** - Robust error management for various scenarios

## Prerequisites

- Python 3.10 or higher

## Installation Options

### Option 1: Package Installation (Recommended)

The easiest way to install the Fastn server is using pip:

```bash
pip install fastn-mcp-server
```

To find the exact path of the installed command:
- On macOS/Linux: `which fastn-mcp-server`
- On Windows: `where fastn-mcp-server`

## After Package Installation

```bash
{
  "mcpServers": {
      "fastn": {
          "command": "fastn-mcp-server",
          "args": [
              "--api_key",
              "YOUR_API_KEY",
              "--space_id",
              "YOUR_WORKSPACE_ID"
          ]
      }
  }
}
```

### Option 2: Manual Setup

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# macOS/Linux: Install UV, create virtual environment, and install dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh && uv venv && source .venv/bin/activate && uv pip install -e .

# Windows (PowerShell): Install UV, create a virtual environment, and install dependencies
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" && uv venv && .venv\Scripts\activate && uv pip install -e .

# Install dependencies directly
uv pip install "httpx>=0.28.1" "mcp[cli]>=1.2.0"
```

## Fastn Account Setup

1. Login to your Fastn account
2. Go to "Connectors" from the left sidebar
3. Activate the service(s) you want to use
4. Go to "Settings" from the left sidebar
5. Click on "Generate API Key" and save it (if using API Key auth)
6. Copy your Workspace ID from the top bar

## Running the Server

The server supports two authentication methods:

### Authentication Method 1: API Key

```bash
# Package installation
fastn-mcp-server --api_key YOUR_API_KEY --space_id YOUR_WORKSPACE_ID

# Manual installation
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_WORKSPACE_ID
```

### Authentication Method 2: Tenant-based

```bash
# Package installation
fastn-mcp-server --space_id YOUR_WORKSPACE_ID --tenant_id YOUR_TENANT_ID --auth_token YOUR_AUTH_TOKEN

# Manual installation
uv run fastn-server.py --space_id YOUR_WORKSPACE_ID --tenant_id YOUR_TENANT_ID --auth_token YOUR_AUTH_TOKEN
```

## Integration with AI Assistants

### Claude Integration

1. Open the Claude configuration file:
   - Windows: `notepad "%APPDATA%\Claude\claude_desktop_config.json"` or `code "%APPDATA%\Claude\claude_desktop_config.json"`
   - Mac: `code ~/Library/Application\ Support/Claude/claude_desktop_config.json`

2. Add the appropriate configuration:

#### Using Package Installation

```json
{
    "mcpServers": {
        "fastn": {
            "command": "/path/to/fastn-mcp-server",
            "args": [
                "--api_key",
                "YOUR_API_KEY",
                "--space_id",
                "YOUR_WORKSPACE_ID"
            ]
        }
    }
}
```

Or with tenant authentication:

```json
{
    "mcpServers": {
        "fastn": {
            "command": "/path/to/fastn-mcp-server",
            "args": [
                "--space_id",
                "YOUR_WORKSPACE_ID",
                "--tenant_id",
                "YOUR_TENANT_ID",
                "--auth_token",
                "YOUR_AUTH_TOKEN"
            ]
        }
    }
}
```

#### Using Manual Installation

API Key authentication:

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

Tenant authentication:

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
                "--space_id",
                "YOUR_WORKSPACE_ID",
                "--tenant_id",
                "YOUR_TENANT_ID",
                "--auth_token",
                "YOUR_AUTH_TOKEN"
            ]
        }
    }
}
```

### Cursor Integration

1. Open Cursor settings
2. Click on "MCP" in the settings menu
3. Click on "Add New"
4. Add a name for your server (e.g., "fastn")
5. Select "Command" as the type
6. Add the command based on your installation:

#### Using Package Installation

API Key authentication:
```
/path/to/fastn-mcp-server --api_key YOUR_API_KEY --space_id YOUR_WORKSPACE_ID
```

Tenant authentication:
```
/path/to/fastn-mcp-server --space_id YOUR_WORKSPACE_ID --tenant_id YOUR_TENANT_ID --auth_token YOUR_AUTH_TOKEN
```

#### Using Manual Installation

API Key authentication:
```
/path/to/your/uv --directory /path/to/your/fastn-server run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_WORKSPACE_ID
```

Tenant authentication:
```
/path/to/your/uv --directory /path/to/your/fastn-server run fastn-server.py --space_id YOUR_WORKSPACE_ID --tenant_id YOUR_TENANT_ID --auth_token YOUR_AUTH_TOKEN
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

## Support

- Documentation: [https://docs.fastn.ai](https://docs.fastn.ai)
- Community: [https://discord.gg/Nvd5p8axU3](https://discord.gg/Nvd5p8axU3)

## License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.
