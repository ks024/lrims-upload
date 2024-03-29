## Project based on automation of a web application where certain local files are uploaded to the server.

```python
python move_file.py \
    --source_dir=/home/user/Documents/source_dir \
    --dest_dir=/home/user/Documents/dest_dir
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