import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        humidity = data["current_condition"][0]["humidity"]
        weather = data["current_condition"][0]["weatherDesc"][0]["value"]

        print("\nWeather Information")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)

    else:
        print("Failed to fetch data.")

except requests.exceptions.RequestException:
    print("Error connecting to API.")
