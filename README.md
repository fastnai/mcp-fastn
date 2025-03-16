# Fastn Server

A simple MCP fastn server implementation that dynamically registers and executes tools based on API definitions. This project includes two server implementations:
- `fastn-claude.py` - Server implementation for Claude.ai
- `fastn-cursor.py` - Server implementation for Cursor.ai

## Prerequisites

- Python 3.10 or higher

## Quick Start

### macOS

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# Install UV, create virtual environment, and install dependencies in one go
curl -LsSf https://astral.sh/uv/install.sh | sh && uv venv && source .venv/bin/activate && uv pip install -e .

# Run Claude server
uv run fastn-claude.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID

# OR run Cursor server
uv run fastn-cursor.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID
```

### Windows

```bash
# Clone repository and navigate to directory
git clone <your-repo-url> && cd fastn-server

# Install UV, create virtual environment, and install dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh && uv venv && .venv\Scripts\activate && uv pip install -e .

# Run Claude server
uv run fastn-claude.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID

# OR run Cursor server
uv run fastn-cursor.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID
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
uv run fastn-cursor.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID
```

## Configuration

You'll need the following credentials to run the server:

- API Key from Fastn
- Space ID from your Fastn your workspace

Optional: You can also specify a use case:
```bash
uv run fastn-claude.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID --usecase "YOUR_USE_CASE"
# OR
uv run fastn-cursor.py --api_key YOUR_API_KEY --space_id YOUR_SPACE_ID --usecase "YOUR_USE_CASE"
```

## Project Structure

- `fastn-claude.py` - Server implementation for Claude.ai
- `fastn-cursor.py` - Server implementation for Cursor.ai
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Dependency lock file
- `.python-version` - Python version specification

## Features

- Dynamic tool registration from Fastn API
- Asynchronous tool execution
- Pydantic model generation for parameter validation
- Logging support
- Command-line argument parsing

## Error Handling

The server includes comprehensive error handling for:
- HTTP requests
- Tool registration
- Parameter validation
- Tool execution

## Logging

Logs are output with timestamp, level, and message in the following format:
```
%(asctime)s - %(levelname)s - %(message)s
```

## Dependencies

- httpx: HTTP client
- mcp[cli]: MCP server implementation
- pydantic: Data validation
