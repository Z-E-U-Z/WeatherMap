import requests

def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from the API.")
        return None

def main():
    weather_data = get_weather_data()
    if weather_data:
        while True:
            print("Options:")
            print("1. Get weather")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                date = input("Enter the date in YYYY-MM-DD HH:00:00 (24hr Time Format): ")
                for data in weather_data['list']:
                    if date in data['dt_txt']:
                        print(f"Temperature on {date}: {data['main']['temp']} Kelvin")
                        break
                else:
                    print("Data not available for the specified date.")
            elif choice == '2':
                date = input("Enter the date in YYYY-MM-DD HH:00:00 (24hr Time Format): ")
                for data in weather_data['list']:
                    if date in data['dt_txt']:
                        print(f"Wind Speed on {date}: {data['wind']['speed']} m/s")
                        break
                else:
                    print("Data not available for the specified date.")
            elif choice == '3':
                date = input("Enter the date in YYYY-MM-DD HH:00:00 (24hr Time Format): ")
                for data in weather_data['list']:
                    if date in data['dt_txt']:
                        print(f"Pressure on {date}: {data['main']['pressure']} hPa")
                        break
                else:
                    print("Data not available for the specified date.")
            elif choice == '0':
                print("Exiting the program.")
                break
            else:
                print("Enter a Valid Choice")

if __name__ == "__main__":
    main()
