from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import requests
url_github_users = "https://api.github.com/users/"

app = Flask(__name__, static_url_path='/public')

@app.route("/")
def index():
    return render_template("index.html", title="GitHub user", data_user="")

@app.route("/get_user", methods=['POST'])
def search_user():
    if request.method == 'POST':
        user = request.form['user']
        request_user = requests.get(url_github_users + user)
        data_user = request_user
        if data_user.status_code == 200:
            return render_template("index.html", data_user=data_user)
    else:
        return render_template("index.html", data_user="")

def data_user_github(info):
    return info

if __name__ == '__main__':
    app.run(debug=True)