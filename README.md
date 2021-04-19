# UOCIS322 - Project 2 #

A "getting started with Docker" project for CIS 322, Introduction to Software Engineering, at the University of Oregon.

NOTE: This project is going to require Docker, therefore use * testium * instead of the default development server (ix-dev).
NOTE: Should you experience a permission error while using Docker on the server, email systems and ask them to "add you to the docker group".

## Getting started

* Go to the web folder in the repository. Read every line of the docker file and the simple flask app.

* Build the simple flask app image using

  ```
  docker build -t your-name-cis322-2 .
  ```
  **Make sure to use a unique name if you're running on testium.**
* Run the container using

  ```
  docker run -d -p port:5000 your-name-cis322-2
  ```
NOTE: Make sure to specify a free port here.
* Launch `http://hostname:port` using your web browser and check the output "UOCIS docker demo!".

## Tasks

* The goal of this project is to implement the same "file checking" logic that you implemented in Project 1, but using Flask.

* Like Project 1, if a file (`name.html`) exists, transmit `200/OK` header followed by that file html. If the file doesn't exist, transmit an error code in the header along with the appropriate page html in the body. You'll do this by creating error handlers that will be (or are) taught in class (refer to the recordings if needed). You'll also create the following two html files with the error messages:
    * `404.html` will display "File not found!"
    * `403.html` will display "File is forbidden!"

* Update your name and email in the `Dockerfile`.

* You will submit your credentials.ini in Canvas. It should include your name and repo URL.

## Grading Rubric
* If your code works as expected: 100 points.

* For every wrong functionality (i.e., (a), (b), and (c) from project 1), 20 points will be docked off.

* If none of the functionalities work, 40 points will be given assuming
    * the credentials.ini is submitted with the correct URL of your repo,
    * the `Dockerfile` builds without any errors, and
    * if the two html files (`404.html` and `403.html`) are created in the appropriate location.

* If the `Dockerfile` doesn't build or is missing, 20 points will be docked off.

* If the two html files are missing, 20 points will be docked off.

* If `credentials.ini` is not submitted or the repo is not found, 0 will be assigned.

## Basic Docker commands

* Get information about docker setup the machine

  ```
  docker info
  ```

* List running docker containers

  ```
  docker ps
  ```

* List all docker containers

  ```
  docker ps -a
  ```

* List images using

  ```
  docker images
  ```

* Build an image

  ```
  docker build -t <Tag name> path/
  ```

  or just do this if your `Dockerfile` is in the same directory:
  ```
  docker build -t <Tag Name> .
  ```

* Remove containers

  ```
  docker container rm <Container Name>
  ```

* Run containers
  ```
  docker run <Tag Name / Image ID>
  ```

  ```
  docker run -h CONTAINER1 -i -t debian /bin/bash
  docker run -h CONTAINER1 -i -t ubuntu /bin/bash
  ```

  Here, `-h` is used to specify a container name, `-t` to start with tty, and `-i` means interactive. Note: second times will be quick because of caching.

* Docker with networking

  ```
  docker run -h CONTAINER2 -i -t --net="bridge" debian /bin/bash
  ```

* When the containers are not running and when you're done, kill them using

  ```
  docker rm `docker ps --no-trunc -aq`
  ```

* Rename using

  ```
  docker rename name_v0 name_v1
  ```

* Start a container

  ```
  docker start <container name>
  ```

* Stop a container

  ```
  docker stop <container name>
  ```

# Creating images

* Create a `Dockerfile`. The name is case sensitive and it has to be `Dockerfile`

  ```
  vim Dockerfile
  ```

* The `FROM` command specifies the base image you are going to use. It can be an existing image, like ubuntu, alpine, debian, etc.

  ```
   FROM debian
  ```

* `CMD` command specifies all the commands you need to run

  ```
   CMD echo hello world
  ```

* Build the image with folder name (`.` in this case)

  ```
   docker build .
  ```

* Final output
  ```
  Successfully built e2e741ea5f6f  
  ```

* Run the image using the image ID (`e2e741ea5f6f` in this case) and a test name of your choice

  ```
  docker run --name <test name> e2e741ea5f6f
  ```

* Remove images using

  ```
  docker rmi <Image ID>
  ```

For more info refer to: https://docs.docker.com/engine/reference/builder/.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
