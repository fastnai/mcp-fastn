# Docker Deployment for Fastn MCP Server

This guide explains how to deploy the Fastn MCP (Model Context Protocol) server using Docker.

## Prerequisites

- Docker and Docker Compose installed
- Fastn API key and Space ID (from your Fastn account)

## Quick Start

### Option 1: Using Docker Compose (Recommended)

1. Create a `.env` file in the project directory with your credentials:

```
API_KEY=your_fastn_api_key_here
SPACE_ID=your_fastn_space_id_here
```

2. Run the server using Docker Compose:

```bash
docker-compose up -d
```

This will build the Docker image and start the container in detached mode.

3. Check the logs:

```bash
docker-compose logs -f
```

### Option 2: Using Docker Directly

1. Build the Docker image:

```bash
docker build -t fastn-mcp-server \
  --build-arg API_KEY=your_fastn_api_key_here \
  --build-arg SPACE_ID=your_fastn_space_id_here .
```

2. Run the container:

```bash
docker run -d --name fastn-mcp-server fastn-mcp-server
```

Alternatively, you can pass the credentials as arguments:

```bash
docker run -d --name fastn-mcp-server fastn-mcp-server "your_fastn_api_key_here" "your_fastn_space_id_here"
```

3. Check the logs:

```bash
docker logs -f fastn-mcp-server
```

## Environment Variables and Arguments

The Dockerfile supports providing the Fastn credentials in multiple ways:

1. Build arguments:
   ```
   --build-arg API_KEY=value --build-arg SPACE_ID=value
   ```

2. Environment variables when running the container:
   ```
   -e API_KEY=value -e SPACE_ID=value
   ```

3. Command line arguments when running the container:
   ```
   docker run fastn-mcp-server "api_key" "space_id"
   ```

## Integration with External Services

### Claude AI

To connect Claude AI to your Docker container:

1. First, build the Docker image:
   ```bash
   docker build -t fastn-mcp-server .
   ```

2. Locate your Claude configuration file:
   - **MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

3. Replace the existing configuration with:

```json
{
  "mcpServers": {
    "fastn": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "API_KEY",
        "-e",
        "SPACE_ID",
        "fastn-mcp-server"
      ],
      "env": {
        "API_KEY": "your_fastn_api_key_here",
        "SPACE_ID": "your_fastn_space_id_here"
      }
    }
  }
}
```

4. Save the file and restart Claude.

5. Claude will now run the Docker container automatically when needed, passing your API key and space ID as environment variables.

### Cursor AI

For Cursor AI integration, update the MCP server configuration to point to your deployed container's URL. 