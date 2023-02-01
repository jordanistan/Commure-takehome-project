<div align="center" id="top"> 
  <img src="./Hero-Image.png" alt="Commure" />

  &#xa0;

  <!-- <a href="https://commure.netlify.app">Demo</a> -->
</div>

<h1 align="center">Commure</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jordanistan/commure?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jordanistan/commure?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jordanistan/commure?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jordanistan/commure?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/jordanistan/commure?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/jordanistan/commure?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/jordanistan/commure?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Commure 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jordanistan" target="_blank">Author</a>
</p>

<br>

## :dart: Apps Security Engineer Assessment ##

Automate the process of launching a container. This container should be running a service that
returns some sort of HTML (“Hello World”) when browsed from localhost.
Assumptions:



## :sparkles: Features ##

The core of the tool will be some code (Python, .Net, etc.) that can be executed and that will
connect to the docker API (or other container daemon) and launch a container running apache
(or web server of choice) to deliver a single web page. There is no need for dynamic input, all
variables can be static.

## :rocket: Technologies ##

The following tools were used in this project:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python's PYPI](https://pypi.org/project/docker/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/jordanistan/commure

# Access
$ cd commure

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python3 main.py  

# The server will initialize in the <http://localhost:80>
```
## Output when testing 


$ python3 main.py
 
 Here is what the python script will output:

 ```bash
#############################################################################################################/n
Go to http://localhost:80 in a browser to see the website!
Container ID:  d66d5afdf942e733c050cb57bd4318b9f75943a5490369c2f19adba9ea63e803
Container Status:  running
#############################################################################################################
```
Let's `curl localhost` to make sure we are seeing the HTML output of the docker container. 

$ curl localhost:80

```bash
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
```
## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/jordanistan" target="_blank">Jordan Robison</a>

&#xa0;

<a href="#top">Back to top</a>
