from boggle import Boggle
from flask import Flask,render_template,session,request,jsonify,redirect

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

scores = []
words = []
@app.route("/", methods=['POST','GET'])
def display_board():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("board.html",board = board)

@app.route("/process", methods=["POST"])
def proc():
    word = request.json['data']['word']
    if word not in words:
        words.append(word)
        code = Boggle().check_valid_word(session["board"], word)
        print(code)
        json = {'result': code}
        return jsonify(json)
    else:
        json = {'result': 'Word already entered'}
        return jsonify(json)
@app.route("/score",methods=["POST"])
def score():
    score = request.json['data']
    scores.append(score)
    json = {'score':score['score']}
    return jsonify(json)