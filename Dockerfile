FROM python:3.9-slim

# Install system dependencies for Ursina and X11 forwarding
RUN apt-get update && apt-get install -y \
    xvfb \
    x11-utils \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy game files
COPY . .

# Set environment variable for display
ENV DISPLAY=:99

# Create a script to run the game with Xvfb
RUN echo '#!/bin/bash\nXvfb :99 -screen 0 1024x768x24 -ac &\npython duck_hunt.py' > /app/start_game.sh && \
    chmod +x /app/start_game.sh

# Command to run the game
CMD ["/app/start_game.sh"]
