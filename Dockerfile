FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY . /app

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Upgrade pip and install uv and project dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir uv \
    && pip install --no-cache-dir -e .

# Expose a port if necessary (not strictly needed for UCL stdio MCP servers)

# Use entrypoint script to handle different configuration modes
ENTRYPOINT ["/app/entrypoint.sh"]