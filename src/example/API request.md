## API request

## Can you explain how an API request and response works with an example?
An API request is a message sent by a client to an API to retrieve or manipulate data. The request typically includes an HTTP method (such as GET, POST, PUT, or DELETE), a URI, and a set of headers. The client sends the request to the API server, which processes it and sends back a response. The response typically includes a status code (such as 200 OK or 404 Not Found), a set of headers, and a body.

* Here's an example of a simple API request and response using the Python requests library:

```python
import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()
print(data)
```

In this example, the get function sends a GET request to the URI https://jsonplaceholder.typicode.com/posts/1. The API server responds with a JSON object containing the data for the post with ID 1.

## How does API automation testing works?
API automation testing is the process of using software to automatically test the functionality of an API. This is typically done by writing test scripts that send a series of requests to the API and check the responses for correctness.

Here's an example of a simple API automation test using the Python testing framework unittest:

```python
import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_get_post_by_id(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)

```

## How does API integration work?
API integration is the process of connecting multiple APIs together to create a seamless experience for the end-user. This typically involves making API calls from one API to another, and passing data between them.

Here's an example of API integration using Python to retrieve data from a weather API and a geolocation API:

```python
import requests
response = requests.get('https://ipapi.co/json')
data = response.json()
lat = data['latitude']
lon = data['longitude']
weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=YOUR_APP_ID')
weather_data = weather_response.json()
print(weather_data)
```


In this example, the first get call is made to https://ipapi.co/json to retrieve the user's geolocation. Then, using the latitude and longitude data, another API call is made to https://api.openweathermap.org/data/2.5/weather to retrieve the current weather data for that location.

