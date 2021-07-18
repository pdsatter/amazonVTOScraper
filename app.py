from flask import Flask, request, render_template

app = Flask('Amazon Time Web-Scraper')


@app.route('/')
def defaultWebsite():
    return render_template('base.html')


@app.route('/home')
def homepage():
    return render_template('homepage.html')
