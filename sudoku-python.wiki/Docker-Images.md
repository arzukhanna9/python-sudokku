## Writing Dockerfile

Source: [Dockerfile](Dockerfile)

* `FROM` specifies the base image on which the docker image will be built.
* `COPY` add files from the Docker client’s current directory.
* `RUN` specifies the additional commands to execute.
* `ENTRYPOINT` sets parameters that will execute (these) cannot be overwritten 
  from the command line. 
* `CMD` sets default commands and/or parameters, which can be overwritten from 
  the command line when docker container runs.

## Building Image Locally

1. Build dockerfile and start executing the commands.

```bash
docker build --tag python-sudoku .
```

2. Run the dockerfile.

```bash
docker run python-sudoku ./solve_sudoku.py <data file>
```

## Pushing Image to Docker Hub

```bash
docker tag python-sudoku arzukhanna/python-sudoku
docker push arzukhanna/python-sudoku
```

## Pulling Image from Docker Hub

```bash
docker pull arzukhanna/python-sudoku
docker run arzukhanna/python-sudoku:latest ./solve_sudoku.py <data file>
```

## Other Commands

* Removing container: `docker rm <container name>`
* Remove images: `docker rmi <image name>`