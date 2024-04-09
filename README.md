# back4app-deploy-ml-model

Learn how to deploy a simple ML model to [Back4app Containers](https://www.back4app.com/container-as-a-service-caas) using [FastAPI](https://fastapi.tiangolo.com/) & [Docker](https://www.docker.com/).

To learn more check out the [article](#).

## Development Setup

1. Clone the repository.

2. Install the dependencies:
    ```sh
    $ pip install -r requirements.txt
    ```
   
3. Run the FastAPI server:
    ```sh
    $ uvicorn app.main:app --reload
    ```
   
4. Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your favorite web browser.

## Deploy (Docker)

1. Install Docker (if you don't have it yet).

2. Build and tag the image:
    ```sh
    $ docker build -t iris-webapp:1.0 .
    ```

3. Start a new container:
   ```sh
    $ docker run -p 80:80 --name iris-webapp iris-webapp:1.0
    ```

4. Navigate to [http://localhost/](http://localhost/) in your favorite web browser.
