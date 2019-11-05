from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/alarm_clock')
def get_alarm_clock_page():
    return render_template("alarm_clock.html", title=get_data()[0]['title'], text=get_data()[0]['text'],
                           count=len(get_data()[0]['text'].split()))


@app.route('/battery_charger')
def get_battery_charger_page():
    return render_template("battery_charger.html", title=get_data()[5]['title'], text=get_data()[5]['text'],
                           count=len(get_data()[5]['text'].split()))


@app.route('/calculator')
def get_calculator_page():
    return render_template("calculator.html", title=get_data()[3]['title'], text=get_data()[3]['text'],
                           count=len(get_data()[3]['text'].split()))


@app.route('/coffeemaker')
def get_coffeemaker_page():
    return render_template("coffeemaker.html", title=get_data()[4]['title'], text=get_data()[4]['text'],
                           count=len(get_data()[4]['text'].split()))


@app.route('/headphones')
def get_headphones_page():
    return render_template("headphones.html", title=get_data()[1]['title'], text=get_data()[1]['text'],
                           count=len(get_data()[1]['text'].split()))


@app.route('/ipod')
def get_ipod_page():
    return render_template("ipod.html", title=get_data()[2]['title'], text=get_data()[2]['text'],
                           count=len(get_data()[2]['text'].split()))


@app.route('/author')
def get_author_page():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
