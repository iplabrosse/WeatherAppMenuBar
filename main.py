import requests
import tempfile
import rumps

# Assuming UNITS and API_KEY are defined globally
UNITS = 'imperial'  # Example unit
API_KEY = ''  # Replace with your actual OpenWeatherMap API key

def get_weather(city_name, zipcode):
    # Corrected URL formation with proper query parameter separation
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&q={city_name}&units={UNITS}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]
        temperature = round(data['main']['temp'])
        description = weather['description'].capitalize()
        icon_url = f'https://openweathermap.org/img/wn/{weather["icon"]}.png'
        return f'{city_name}, {zipcode}: {temperature}°F, {description}', icon_url
    else:
        # Improved error handling
        error_message = data.get("message", "Unknown error")
        return f'Error fetching weather data for {city_name}, {zipcode}: {error_message}', None

class WeatherApp(rumps.App):
    def __init__(self):
        super(WeatherApp, self).__init__('WeatherApp')
        self.icon = 'icon.png'

    @rumps.clicked('Search')
    def search_weather(self, _):
        user_input = rumps.Window("Enter city name or Zip Code:").run().text
        parts = user_input.split(',')
        if len(parts) == 1 or len(parts) == 2:
            city_name = parts[0].strip()
            zipcode = parts[1].strip() if len(parts) == 2 else None
            weather_info, icon_url = get_weather(city_name, zipcode)
            if icon_url:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
                    tmp_file.write(requests.get(icon_url).content)
                    self.icon = tmp_file.name
            self.title = weather_info
        else:
            self.title = 'Invalid input. Please enter a city name or zipcode.'

    @rumps.timer(1800)
    def auto_refresh(self, _):
        if self.title and ':' in self.title:
            parts = self.title.split(':')
            city_name = parts[0].strip()
            weather_info, icon_url = get_weather(city_name, None)  # Assuming zipcode is not used here
            if icon_url:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
                    tmp_file.write(requests.get(icon_url).content)
                    self.icon = tmp_file.name
            self.title = weather_info
if __name__ == '__main__':
    app = WeatherApp()
    app.run()
    