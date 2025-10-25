# f25-docker-recitation

## 1. Running the app locally
In the root directory, run:

```terminal
pip install -r requirements.txt
```
to install requirements.

```terminal
uvicorn app.main:app --host 0.0.0.0 --port 8080
```
to locally run the app.

## 2. Build the docker image
Make sure your have `Dockerfile`
```terminal
docker build -t myimage .
```

## 3. Local or remote containerization (and deployment)
### Local
You can containerize locally two ways. Using `docker run` or using the `docker-compose.yml` file.
```terminal
docker run -d --name mycontainer -p 80:80 myimage 
```

OR

```terminal
docker-compose up -d
```

### Remote
Instructions from [here](https://fly.io/docs/languages-and-frameworks/dockerfile/).
1. The `fly launch` command detects `Dockerfile` and builds it.
```terminal
fly launch
```

2. Deploy the application with fly.
```terminal
fly deploy
```