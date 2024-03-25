WeatherApp is a simple desktop application built with Python that allows users to check the current weather conditions for a specified city or zip code. The application uses the OpenWeatherMap API to fetch weather data and displays it directly on your desktop.

Features Search for weather information by city name or zip code. Automatically refreshes weather data every 30 minutes. Displays weather conditions and temperature. Updates the app icon with the current weather condition icon. Prerequisites Before you begin, ensure you have met the following requirements:

Python 3.x installed on your machine. An active internet connection to fetch weather data. An API key from OpenWeatherMap (You can obtain one by signing up at OpenWeatherMap). Installation To install WeatherApp, follow these steps:

Clone the repository to your local machine: git clone https://github.com/iplabrosse/WeatherApp.git Navigate to the project directory: cd WeatherApp Install the required Python packages: pip install -r requirements.txt Configuration Before running the application, you need to set up your OpenWeatherMap API key. Open main.py and replace API_KEY with your actual API key.

Running the Application To run WeatherApp, execute the following command in the project directory:

python main.py Usage Click on the "Search" button in the app menu. Enter the city name or zip code in the input window that appears. Press "OK" to fetch and display the weather information. Contributing Contributions to WeatherApp are welcome. To contribute:

Fork the repository. Create a new branch (git checkout -b feature/AmazingFeature). Commit your changes (git commit -m 'Add some AmazingFeature'). Push to the branch (git push origin feature/AmazingFeature). Open a pull request.
