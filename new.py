import requests

def get_temperature(city: str) -> str:
    """
    Fetches the current temperature for a given city.
    :param city: Name of the city (e.g., "London").
    :return: Current temperature in Celsius or an error message.
    """
    api_key = "9740dc8081614910ab7f44b33781a112"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        temperature = data["main"]["temp"]
        return f"The current temperature in {city} is {temperature}°C."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return "Unable to retrieve temperature. Please check the city name."
temp =get_temperature(city="Kathmandu")
print(temp)