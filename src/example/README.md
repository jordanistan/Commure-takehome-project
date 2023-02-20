Here's an example of a Dockerfile that implements various hardening measures as recommended by the Center for Internet Security (CIS) Docker 1.13.0 benchmark:

```bash
# Start with a base image
FROM alpine:3.12

# Set the user and group to run Docker processes
# This reduces the attack surface by running the processes as non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Update the package index and install required packages
RUN apk update && apk add --no-cache \
  su-exec \
  curl

# Copy the application code into the image
COPY app /app

# Set the working directory to the location of the application code
WORKDIR /app

# Run the application as non-root user
RUN chown -R appuser:appgroup /app

# Specify the user to run the application
USER appuser

# Expose the port for the application to listen on
EXPOSE 80

# Define the command to run when the container starts
CMD ["./run.sh"]
```
In this example:

The base image is alpine:3.12, which is a minimal Linux distribution.
The Docker processes are run as the appuser and appgroup user and group, respectively, instead of root.
The application code is copied into the image and the working directory is set to the location of the code.
The appuser user is specified to run the application.
The exposed port is set to 80.
Note: The ./run.sh command in the CMD instruction should be replaced with the appropriate command to run your application.