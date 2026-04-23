import requests

def get_weather(city_name, latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current_weather = data.get("current_weather")
        if not current_weather:
            print("Weather data is missing from the response.")
            return

        temperature = current_weather.get("temperature")
        windspeed = current_weather.get("windspeed")
        weathercode = current_weather.get("weathercode")
        time = current_weather.get("time")

        print(f"Current weather for {city_name}")
        print(f"Time: {time}")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {windspeed} km/h")
        print(f"Weather Code: {weathercode}")

    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the API.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError:
        print("Could not decode the API response.")

def main():
    city_name = "New York"
    latitude = 40.7128
    longitude = -74.0060
    get_weather(city_name, latitude, longitude)

if __name__ == "__main__":
    main()