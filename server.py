from flask import Flask, render_template, request

from weather import get_weather

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

    _weather = get_weather(city)
    if not _weather['cod'] == 200:
        return render_template("not-found.html")

    return render_template(
        "weather.html",
        title=_weather["name"],
        status=_weather["weather"][0]["description"].capitalize(),
        temp=f"{_weather['main']['temp']:.1f}",
        feels_like=_weather['main']['feels_like']
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
