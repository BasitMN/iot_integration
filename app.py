from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route('/sensor-data', methods=['POST'])
def sensor_data():
    data = request.get_json()

    # Validera mot kontraktet
    if 'device' not in data or 'temp' not in data:
        return jsonify({'status': 'error', 'message': 'device och temp krävs'}), 400
    if not isinstance(data['temp'], (int, float)):
        return jsonify({'status': 'error', 'message': 'temp måste vara ett tal'}), 400

    database.save_reading(data['device'], data['temp'])
    return jsonify({'status': 'ok'})

@app.route('/temperature')
def temperature():
    return jsonify(database.get_readings())

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True, port=5000)