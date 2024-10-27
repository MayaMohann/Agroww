from flask import Flask
from flask import  redirect, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    title='Home'
    return render_template('index.html',title=title)
