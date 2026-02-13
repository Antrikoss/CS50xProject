from flask import Flask, render_template, request, session
from datetime import datetime
import requests

app = Flask(__name__)

# API key & secret key
API_key = "API_key"
app.secret_key = "Secret_key"


@app.route("/", methods=["GET", "POST"])
def open():
    return render_template("open.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    # Get user's location
    Day = request.args.get("Day", default=0, type=int)
    location = request.args.get("location")

    # Check location
    if location:
        session["location"] = location
    else:
        location = session.get("location")
        if not location:
            return render_template("error.html")

    # Check if input is None
    if "location" in request.args.to_dict():
        if not request.args.get("location"):
            return render_template("error.html")
    # Check if input is number
    if location.isnumeric():
        return render_template("error.html")

    # Get location coordinates
    location_data = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={location}&appid={API_key}"
    )

    # Check for erros
    if not location or not location_data.json():
        return render_template("error.html")

    # Get the weather data
    lat = location_data.json()[0]["lat"]
    lon = location_data.json()[0]["lon"]
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_key}"
    )
    time = datetime.now().hour

    # Funtion which helps to calculates a number that will be used later to retrieve elements from weather data
    def number(time):
        return int((12 - time) / 3)

    # The number mentioned above
    n = number(time) + (Day * 8)

    # Decleration of weather data variables
    icon_key = None
    img_key = None
    location = None
    temperature = None
    humidity = None
    wind_speed = None
    wind_gust = None
    visibility = None
    pressure = None
    weather = None

    # Select the data
    if Day == 0:
        location = location_data.json()[0]["name"]
        temperature = int(round(weather_data.json()["list"][0]["main"]["temp"]))
        humidity = round(weather_data.json()["list"][0]["main"]["humidity"])
        wind_speed = int(round((weather_data.json()["list"][0]["wind"]["speed"] * 36) / 10))
        wind_gust = round((weather_data.json()["list"][0]["wind"]["gust"] * 36) / 10)
        visibility = round(weather_data.json()["list"][0]["visibility"] / 1000, 1)
        pressure = round(weather_data.json()["list"][0]["main"]["pressure"])
        weather = weather_data.json()["list"][0]["weather"][0]["main"]
    else:
        location = location_data.json()[0]["name"]
        temperature = int(round(weather_data.json()["list"][n]["main"]["temp"]))
        humidity = round(weather_data.json()["list"][n]["main"]["humidity"])
        wind_speed = int(round((weather_data.json()["list"][n]["wind"]["speed"] * 36) / 10))
        wind_gust = round((weather_data.json()["list"][n]["wind"]["gust"] * 36) / 10)
        visibility = round(weather_data.json()["list"][n]["visibility"] / 1000, 1)
        pressure = round(weather_data.json()["list"][n]["main"]["pressure"])
        weather = weather_data.json()["list"][n]["weather"][0]["main"]

    # Manipulate the data
    icon_key = weather
    if icon_key == "Clear":
        img_key = "/static/Graphics/Sunny.jpg"
        icon_key = "sunny"
    elif icon_key == "Rain":
        img_key = "/static/Graphics/Rainy.jpg"
        icon_key = "rainy"
    elif icon_key == "Clouds":
        img_key = "/static/Graphics/Clouds.jpg"
        icon_key = "cloud"
    elif icon_key == "Snow":
        img_key = "/static/Graphics/Snow.jpg"
        icon_key = "cloudy_snowing"

    # Link the data for each displayed week day (buttons)
    day0 = []
    day1 = []
    day2 = []
    day3 = []
    day4 = []
    days = [day0, day1, day2, day3, day4]

    for i, day in enumerate(days):
        z = number(time) + (i * 8)
        temp_date = weather_data.json()["list"][z]["dt_txt"]
        day_name = datetime.strptime(temp_date, "%Y-%m-%d %H:%M:%S").strftime("%A")
        day_temp = int(round(weather_data.json()["list"][z]["main"]["temp"]))
        day_date = datetime.strptime(temp_date, "%Y-%m-%d %H:%M:%S").date().day
        day_txt = weather_data.json()["list"][z]["weather"][0]["main"]

        # Implement the data
        if day_txt == "Clear":
            day_txt = "sunny"
        elif day_txt == "Rain":
            day_txt = "rainy"
        elif day_txt == "Clouds":
            day_txt = "cloud"
        elif day_txt == "Snow":
            day_txt = "cloudy_snowing"

        if day_name == "Monday":
            day_name = "Mon"
        if day_name == "Tuesday":
            day_name = "Tue"
        if day_name == "Wednesday":
            day_name = "Wed"
        if day_name == "Thursday":
            day_name = "Thu"
        if day_name == "Friday":
            day_name = "Fri"
        if day_name == "Saturday":
            day_name = "Sat"
        if day_name == "Sunday":
            day_name = "Sun"

        day.append(day_name)
        day.append(day_temp)
        day.append(day_txt)
        day.append(day_date)

    return render_template(
        "index.html",
        location=location,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        wind_gust=wind_gust,
        visibility=visibility,
        pressure=pressure,
        weather=weather,
        days=days,
        img_key=img_key,
        icon_key=icon_key
    )


@app.route("/error", methods=["GET", "POST"])
def error():
    return render_template("error.html")
