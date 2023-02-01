import docker
import os

# Connect to Docker using the default socket or the configuration in your environment:
## Reference: https://pypi.org/project/docker/#:~:text=Connect%20to%20Docker,.from_env()
# import docker
# client = docker.from_env()

client = docker.from_env()

# Create a custom message here; Let's say Commure Rocks! HTML page, and let's center the text and add a button to redirect to the Commure website with a background image. For extra brownie points.. wink wink
index_html = """
<html>
  <head>
    <title>Commure Rocks!</title> 
  </head>
    <style>
      body {
        background-image: url(https://www.commure.com/wp-content/uploads/2022/10/Hero-Image.png);
        background-size: cover;
        background-repeat: no-repeat;
      }
            .center {
        text-align: center;
      }
    </style>
  <body>
    <div class="center">
    <h1>Commure Rocks! WOot WOOt!! </h1>
    <h2> Powered by Awesomeness </h2>
    <button onclick="window.location.href = 'https://www.commure.com/';">Want to know more? Click Me</button>
    </div>
  </body>
</html>
"""

# Write the custom index.html to a file
with open('./index.html', 'w') as file:
    file.write(index_html)

# Create a Dockerfile
dockerfile = """
FROM httpd
COPY index.html /usr/local/apache2/htdocs/
"""

# Write the Dockerfile to disk
with open('./Dockerfile', 'w') as file:
    file.write(dockerfile)

# Build a Docker image from the Dockerfile
image, build_logs = client.images.build(path=os.getcwd(), rm=True, tag="commure-website")

# Launch a container from the image
container = client.containers.run(image, "httpd-foreground", ports={"80/tcp": 80}, detach=True)

# Confirm the container is running and get its information
container.reload()
print(" ")
print(" ")
print("#############################################################################################################/n") 
print("Go to http://localhost:80 in a browser to see the website!") 
print("Container ID: ", container.id)
print("Container Status: ", container.status)
print("#############################################################################################################")

