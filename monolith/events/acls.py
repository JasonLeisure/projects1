import json
import requests
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    # Create a dictionary for the headers to use in the request
    headers = {"Authorization": PEXELS_API_KEY}
    # Define the params for the request as well
    params = {"query": city + "  " + state}
    # Create the URL for the request with the city and state
    url = "https://api.pexels.com/v1/search"
    # Make the request
    response = requests.get(url, params=params, headers=headers)
    # Parse the JSON response
    content = response.content
    parsed_json = json.loads(content)
    picture = parsed_json["photos"][0]["src"]["original"]
    # Return a dictionary that contains a `picture_url` key and
    #   one of the URLs for one of the pictures in the response
    return {"picture_url": picture}


def get_lat_long(location):
    """
    Returns the latitude and longitude for the specificed location
    using the OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{location.city},{location.state.abbreviation},USA",
        "appid": OPEN_WEATHER_API_KEY,
    }
    response = requests.get(base_url, params=params)
    parsed_json = json.loads(response.content)
    return {
        "lattitude": parsed_json[0]["lat"],
        "longitude": parsed_json[0]["lon"],
    }


def get_weather_data(location):
    """
    Returns current weather data for the specified location
    using the OpenWeatherMap API.
    """
    # Get the lat and lon for the location
    lat_long = get_lat_long(location)
    # Get the weather data for the API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat_long["latitude"],
        "lon": lat_long["longitude"],
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    response = requests.get(base_url, params=params)
    # Parse the response object
    parsed_json = json.loads(response.content)
    # Create a new dictionary
    weather_data = {
        "temp": parsed_json["main"]["temp"],
        "description": parsed_json["weather"][0]["description"],
    }

    return weather_data
