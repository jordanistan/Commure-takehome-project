Docker Container Cheatsheet

List all running containers: docker ps
List all containers, including stopped ones: docker ps -a
Start a container: docker start <container_id>
Stop a container: docker stop <container_id>
Remove a container: docker rm <container_id>
Create and start a new container: docker run <image_name>
Create and start a new container with a name: docker run --name <container_name> <image_name>
Create and start a new container with exposed ports: docker run -p <host_port>:<container_port> <image_name>
Create and start a new container with a volume: docker run -v <host_path>:<container_path> <image_name>
Create and start a new container in detached mode: docker run -d <image_name>
Interview Questions:

## What is a Docker container?
A Docker container is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

## How does a Docker container differ from a virtual machine?
A Docker container differs from a virtual machine in that it does not include a separate operating system. Instead, it uses the host operating system's kernel and shares the host system's resources. This makes containers more lightweight and portable than virtual machines.

## How do you list all running containers on a system?
To list all running containers on a system, you can use the command docker ps.

## How do you start a stopped container?
You can start a stopped container using the command docker start <container_id>.

## How do you remove a container?
You can remove a container using the command docker rm <container_id>.

A Dockerfile is a script that contains instructions for building a Docker image. It is used to automate the process of creating an image from a base image, adding software and dependencies, and configuring the environment.

Here's an example of a simple Dockerfile that copies an application from the host machine to the container and runs it on port 8080:
```bash
# Use an existing node image as a base
FROM node:12

# Set the working directory
WORKDIR /usr/src/app

# Copy the app files from the host machine to the container
COPY . .

# Install dependencies
RUN npm install

# Expose the app's port
EXPOSE 8080

# Run the app
CMD ["npm", "start"]

```


This Dockerfile starts by using the official Node.js 12 image as the base image. It then sets the working directory to /usr/src/app, where the application files will be copied. Next, it copies the files from the host machine to the container using the COPY command. Then it runs npm install to install the dependencies. After that it exposes port 8080, then runs the command to start the app.

To build an image from this Dockerfile, you can run the command:
```bash
docker build -t myapp .
```
This command will build an image with the tag "myapp" from the current directory where the Dockerfile is.

Finally, to run the container, you can use the following command:

```bash
docker run -p 8080:8080 myapp

```
This command will run the container, mapping port 8080 on the host machine to port 8080 in the container. The app will be accessible on port 8080 on the host machine.