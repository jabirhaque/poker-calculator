from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def get_name():
    return jsonify({'name': 'Jabir'})

if __name__ == '__main__':
    app.run()