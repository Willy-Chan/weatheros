# Weatheros
Weatheros is a web application that provides weather information for the fictional locations in Westeros from the popular series Game of Thrones. Developed using Python's Flask framework, it utilizes the user's geolocation data to determine their current location and delivers the temperature in a corresponding Westeros location.

## Example
![image](https://github.com/Willy-Chan/weatheros/assets/106504264/b88a92ba-02f4-4051-9e51-ab568930b17b)

## Settings
If `weather_condition` is equal to "Rain" or "Drizzle":
- Location: The Iron Islands

Else if `temp` is greater than or equal to 30:
- Location: Dorne

Else if `temp` is less than 0:
- Location: Beyond the Wall

Else if `weather_condition` is equal to "Snow":
- Location: Winterfell

Else if `weather_condition` is equal to "Clear":
- If `temp` is greater than 20:
  - Location: King's Landing

- Else:
  - Location: The Wall

Else if `weather_condition` is equal to "Clouds":
- If `temp` is greater than 20:
  - Location: Braavos
- Else:
  - Location: The North

Else if `weather_condition` is equal to "Thunderstorm":
- Location: Meereen

Else:
- Location: Unknown Location


## Installation

Before you can run  weatheros, ensure you have Python 3.6 or later installed on your machine. Then, follow these steps: 
1. Clone the repository:

```bash
git clone https://github.com/willy-chan/Flask-Westeros-Weather-App.git
``` 
2. Change into the project directory:

```bash
cd weatheros
``` 
3. Create a virtual environment:

```
python3 -m venv venv
``` 
4. Activate the virtual environment: 
- On Windows:

```
venv\Scripts\activate
``` 
- On macOS/Linux:

```bash
source venv/bin/activate
``` 
5. Install required packages:

```
pip install -r requirements.txt
``` 
6. Set environment variables: 
- On Windows:

```arduino
set FLASK_APP=app.py
set FLASK_ENV=development
``` 
- On macOS/Linux:

```arduino
export FLASK_APP=app.py
export FLASK_ENV=development
``` 
7. Run the application:

```arduino
flask run
``` 
8. Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  to access the Weatheros.

## Technologies Used
- Python 3.6+
- Flask
- JavaScript
- Geolocation API
- HTML5
- CSS3
- Bootstrap 5
- Leaflet.js
## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE)  file for details.
## Acknowledgments 
- Weather data for the fictional locations in Westeros is provided by [WesterosWeatherAPI](https://westerosweatherapi.example.com/) . 
- Geolocation service is provided by [GeolocationAPI](https://geolocationapi.example.com/) .
- Map images and location data are sourced from Game of Thrones fandom resources.
## Author

**Willy Chan** - [willy-chan](https://github.com/willy-chan)
