# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from sensor import read_sensor

app = Flask(__name__)
CORS(app)  # permite que o React acesse os dados

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(read_sensor())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
