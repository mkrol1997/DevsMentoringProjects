## To build container image exec in console:
   `docker build -t <image_name> .`
   
## To run container:
    docker run --name <container_name> -v "$(pwd)/flask_app/static/:/app/flask_app/static/" -p 8000:8000 <image_name>