from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather')
def weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = "Indore"
        
    weather = get_weather(city)
    if not weather['cod'] == 200:
        return render_template("not-found.html")
     
    return render_template(
        "weather.html",
        title=weather["name"],
        status=weather["weather"][0]["description"].capitalize(),
        temp=f"{weather['main']['temp']:.1f}",
        feels_like=weather['main']['feels_like']
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)