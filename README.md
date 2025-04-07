# Fastn Server

The Fastn server is a powerful, scalable platform that enables dynamic tool registration and execution based on API definitions. It seamlessly integrates with services like Claude.ai and Cursor.ai, providing a unified server solution for a wide range of tasks. With its robust architecture, Fastn delivers exceptional performance and flexibility for real-time, API-driven operations.

## Features

- **Integrated platform support** - Use services like Slack, Notion, HubSpot, and many more through the Fastn server after completing the simple setup
- **Logging support** - Comprehensive logging system
- **Error handling** - Robust error management for various scenarios

## Step-by-Step Setup Guide

### Step 1: Fastn Configuration

1. Login to your Fastn account (sign up at [fastn.ai](https://fastn.ai) if you don't have one)
2. Go to "Connectors" from the left sidebar
3. Activate the service(s) you want to use by clicking on activate
4. Go to "Settings" from the left sidebar
5. Click on "Generate API Key" and save it somewhere locally
6. Click on the copy button that exists on the top bar (left side of your profile)
7. Copy your Workspace ID and save it as well

### Step 2: Installation & Setup (Choose One Option)

#### Option A: Package Installation (Recommended)

The recommended way to install the FastN server is using [pipx](https://pypa.github.io/pipx/):

```bash
pipx install fastn-server
```

Alternatively, you can use pip:

```bash
pip install fastn-server
```

To run the server directly:

```bash
fastn-server --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID
```

#### Option B: Manual Setup

##### Prerequisites

- Python 3.10 or higher

##### Setup Steps

###### macOS

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# Install UV, create virtual environment, and install dependencies in one go
curl -LsSf https://astral.sh/uv/install.sh | sh && uv venv && source .venv/bin/activate && uv pip install -e .

# Run server
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID 
```

###### Windows

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# Install UV, create a virtual environment, and install dependencies
# Option 1: Install UV using pip
python -m pip install uv
# Make sure to copy the installation path and add it to your Windows environment variables.

# Option 2: Install UV using PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" && uv venv && .venv\Scripts\activate && uv pip install -e .

# Run server
uv run fastn-server.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID 
```

### Step 3: Integration with AI Assistants

First, find the path to your fastn-server command (if using the package installation):

**macOS/Linux:**
```bash
which fastn-server
```

**Windows:**
```bash
where fastn-server
```

The configuration JSON is the same for both Claude and Cursor. Replace the path with the actual path from the command above:

#### Package Installation Configuration (Option A)

**macOS/Linux example:**
```json
{
    "mcpServers": {
        "fastn": {
            "command": "/Users/username/.local/bin/fastn-server",
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

**Windows example:**
```json
{
    "mcpServers": {
        "fastn": {
            "command": "C:\\Users\\username\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\fastn-server.exe",
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

> **Important note for Windows users:** Make sure to use double backslashes (\\\\) in your path, as shown in the example above. Single backslashes will cause errors in JSON.

#### Manual Installation Configuration (Option B)

**Configuration example:**
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

#### Integration with Claude

1. Open the Claude configuration file:

**Windows:**
```bash
# Using Notepad
notepad "%APPDATA%\Claude\claude_desktop_config.json"

# Using VS Code
code "%APPDATA%\Claude\claude_desktop_config.json"
```

**Mac:**
```bash
# Using TextEdit
open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Using VS Code
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. Add the appropriate configuration JSON based on your installation method.

#### Integration with Cursor

1. Open Cursor settings
2. Click on "MCP" in the settings menu
3. Click on "Add New"
4. Add a name for your server (e.g., "fastn")
5. Select "Command" as the type
6. Use the appropriate configuration based on your installation method

That's it! Your AI assistant now has access to all the tools configured in your FastN workspace.

## Security Considerations

- Keep your API key and Space ID secure
- Use environment variables or a secure configuration file for production deployments
- Regularly rotate your API keys for enhanced security

### Troubleshooting

#### Package Structure Error

If you encounter an error like this during manual installation:
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

## Logging

Logs are output with timestamp, level, and message in the following format:
```
%(asctime)s - %(levelname)s - %(message)s
```

## Support

For questions, issues, or feature requests, please visit:
- Documentation: [https://docs.fastn.ai](https://docs.fastn.ai)
- Community: [https://community.fastn.ai](https://community.fastn.ai)

## License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.