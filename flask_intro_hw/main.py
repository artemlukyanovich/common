from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template('home.html')


@app.route('/vegetables')
def get_vegetables_page():
    return render_template('vegetables.html', vg_list=['beans', 'carrot', 'beetroot', 'cucumber'])


@app.route('/fruits')
def get_fruits_page():
    return render_template('fruits.html', fr_list=['melon', 'apple', 'strawberry', 'grape'])


if __name__ == "__main__":
    app.run(debug=True)
