from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def index():
    source = requests.get(
        "https://ngojobsinafrica.com/?post_type=noo_job&s=&location%5B%5D=zimbabwe&category%5B%5D=information-technology").text
    soup = BeautifulSoup(source, 'lxml')

    return render_template('index.html', **locals())
    app.run(debug=True)


if __name__ == '__main__':
    app.run()
