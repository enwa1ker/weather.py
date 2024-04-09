import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

def get_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')

        current_temp = soup.find("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
        chances_rain = soup.find("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

        if current_temp and chances_rain:
            temp = current_temp.get_text().strip()
            temp_rain = chances_rain.get_text().strip()

            result = f"Current temperature: {temp} in Patna, Bihar\nChance of rain: {temp_rain}"
            return result
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def show_weather_notification(weather_data):
    if weather_data:
        toaster = ToastNotifier()
        toaster.show_toast("Live Weather Update", weather_data, duration=10)
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    url = "https://weather.com/en-IN/weather/today/l/5956a8e19f6f6ea84900c1ada95688899d2c4525c7522e0086c259a64eb0b6d0"
    weather_data = get_weather_data(url)
    show_weather_notification(weather_data)
