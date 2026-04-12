# Webal

Webal is my CS50 final project — a **full-stack weather forecasting web application** built with Flask.  
It allows users to search for any location and view current weather conditions along with a 5-day forecast in a clean and user-friendly interface.

<img width="1301" alt="Screenshot 2026-04-12 104928" src="https://github.com/Antrikoss/CS50xProject/blob/ad42b28d5b5784e6a5530727bb867c64495d1bc4/Screenshot%202026-04-12%20104928.png">

Weather data is provided by [OpenWeather](https://openweathermap.org/).

## 🚀 Features

- **Live Weather Data**  
  Retrieve up-to-date weather information for any location using the OpenWeather API.

- **5-Day Forecast**  
  View detailed weather forecasts, including temperature, wind speed, and humidity.

- **Search Functionality**  
  Easily search for cities worldwide and get instant results.

- **Clean & Responsive UI**  
  Simple and user-friendly interface for browsing weather data.

## 📦 Prerequisites

Make sure you have Python installed, along with the following libraries:

- Flask

- Requests

You can install all dependencies using:
```bash
pip install flask requests
```

## 🛠️ Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/Antrikoss/CS50xProject.git
cd CS50xProject
```

2. Run the Flask app:
```bash
python -m flask run
```

## 📁 Project Structure
```bash
CS50xProject/
|-- static/
|   |-- Graphics/
|   |-- styles.css
|-- templates/
|   |-- error.html
|   |-- index.html
|   |-- layout.html
|   |-- open.html
|-- app.py
|-- README.md
|-- requirements.txt
```
