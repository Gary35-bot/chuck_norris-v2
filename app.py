from flask import Flask
import requests


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_chuck_norris():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return response
