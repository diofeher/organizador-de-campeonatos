from flask import Flask, render_template, request
import itertools
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process/", methods=['POST'])
def process():
    if request.method == 'POST':
        players = [player for player in request.form.getlist('player') if player != '']
        games = itertools.combinations(players, r=2)
        return render_template('championship.html', games=games)