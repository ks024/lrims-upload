## Project based on automation of a web application where certain local files are uploaded to the server.

### Running the script locally.
```python
python move_file.py \
    --source_dir=/home/user/Documents/source_dir \
    --dest_dir=/home/user/Documents/dest_dir
```

### Creating docker image.
#### Create a docker file where script files are located.
## Sample of Dockerfile.
```python
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
```

## Building a docker image.
```bash
docker build -t move-files .
```

## To use the docker image
```bash
docker run -it --rm \
    -v /path/to/source_dir:/app/source_dir \
    -v /path/to/dest_dir:/app/dest_dir \
    move-files \
    --source_dir=/app/source_dir \
    --dest_dir=/app/dest_dir
```
