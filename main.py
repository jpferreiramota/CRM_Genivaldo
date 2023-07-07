from flask import Flask, render_template, g, request, redirect, url_for, session, flash

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro")
def cadastro():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/painel")
def painel():
    return "Esse é o painel."


if __name__ == "__main__":
    app.run()
