from flask import Flask, request, jsonify
from simulation.digital_twin_simulator import simulate_machine

app = Flask(__name__)
@app.route("/")
def index():
    return "Server is running"
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    temp = data["temperature"]
    vibration = data["vibration"]

    result = simulate_machine(temp, vibration)

    return jsonify({"status": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)