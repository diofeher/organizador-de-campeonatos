from flask import Flask, render_template, request
import itertools
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process/", methods=['POST'])
def process():
    if request.method == 'POST':
        players = [player for player in request.form.getlist('player') if player != '']
        games = list(itertools.combinations(players, r=2))
        random.shuffle(games)
        return render_template('championship.html', games=games)
