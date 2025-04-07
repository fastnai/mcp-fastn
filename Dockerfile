FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Set up working directory
WORKDIR /app

# Copy project files
COPY fastn-server.py .
COPY pyproject.toml .
COPY README.md .
COPY LICENSE .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install httpx>=0.28.1 mcp[cli]>=1.2.0 fastapi>=0.112.0 uvicorn>=0.27.0 starlette>=0.36.0

# Create args for API key and space ID
ARG API_KEY=""
ARG SPACE_ID=""
ARG PORT="8000"
ARG HOST="0.0.0.0"

# Set environment variables from args
ENV API_KEY=${API_KEY} \
    SPACE_ID=${SPACE_ID} \
    PORT=${PORT} \
    HOST=${HOST}

# Create entrypoint script to handle args
RUN echo '#!/bin/bash\n\
api_key=${API_KEY:-$1}\n\
space_id=${SPACE_ID:-$2}\n\
port=${PORT:-$3}\n\
host=${HOST:-$4}\n\
\n\
if [ -z "$api_key" ] || [ -z "$space_id" ]; then\n\
  echo "Error: API_KEY and SPACE_ID must be provided either as build args, environment variables, or command-line arguments."\n\
  exit 1\n\
fi\n\
\n\
python fastn-server.py --api_key "$api_key" --space_id "$space_id" --port "$port" --host "$host"\n' > /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command (will be overridden if arguments are passed)
CMD ["", "", "8000", "0.0.0.0"] 