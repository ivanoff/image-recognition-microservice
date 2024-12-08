# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch with CPU support
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=src/server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["python3", "src/server.py"]

