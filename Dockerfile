FROM python:3.12-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Expose the port (if needed)
EXPOSE 8000

# Default command (you can change this to run tests, or use the CLI)
CMD ["bash"]
