# Use a lightweight Python base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY move_file.py .

# Install any dependencies (if needed)
# RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "move_file.py"]