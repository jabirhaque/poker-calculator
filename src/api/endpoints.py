from flask import Flask, jsonify, request

from src.model.card import Card
from src.model.game import Game
from src.service.calculator import probability

app = Flask(__name__)

@app.route('/get_probability', methods=['GET'])
def get_probability():
    pocket = [Card(key) for key in request.args.getlist('pocket')]
    community = [Card(key) for key in request.args.getlist('community')]
    opponent_num = int(request.args.get('opponent_num'))
    game = Game(pocket, community, opponent_num, [])
    return jsonify({'probability': probability(game)[0]})

if __name__ == '__main__':
    app.run()