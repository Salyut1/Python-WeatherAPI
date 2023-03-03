# Weather API Documentation: https://www.weatherapi.com/docs/

import requests
import secrets

def get_weather_data(zip_code):
    """
    Get the current weather data for a specified zip code using WeatherAPI.

    Args:
        zip_code (str): A valid US zip code.

    Returns:
        str: A string containing the current weather data for the specified location,
        including the location name, condition, temperature (in Fahrenheit), and wind speed.
    """

    # Create the URL for the API call
    url = f'http://api.weatherapi.com/v1/current.json?key={secrets.API_KEY}&q={zip_code}'
    
    # Send the GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the relevant data from the JSON response
        data = response.json()
        location = data['location']['name']
        condition = data['current']['condition']['text']
        wind = data['current']['wind_mph']
        temperature_f = data['current']['temp_f']

        # Format the data into a string and return it
        return f"Current weather in {location}: {condition}, {temperature_f}F with a wind speed of {wind}mph."
    else:
        # If the request was not successful, return an error message
        return "An error occurred while getting weather data. Please check the zip code and try again."

# Prompt the user to enter a zip code
user_input = input("Enter the ZIP code of the location (e.g. 90210):\n")

# Keep prompting the user until a valid zip code is entered
while len(user_input) != 5 or not user_input.isdigit():
    print("Invalid input. Please enter a valid 5-digit ZIP code.")
    user_input = input("Enter the ZIP code of the location (e.g. 90210):\n")

# Call the get_weather_data function with the user's input and print the result
print(get_weather_data(user_input))
