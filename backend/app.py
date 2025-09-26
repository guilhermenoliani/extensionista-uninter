# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from sensor import read_sensor as mock_sensor  # mock importado

app = Flask(__name__)
CORS(app)

# Flag para decidir se o sensor real será usado
USE_REAL_SENSOR = False

try:
    import Adafruit_DHT  # tenta importar a lib do DHT11
    SENSOR = Adafruit_DHT.DHT11
    PIN = 4  # ajuste conforme o pino conectado no Raspberry Pi
    USE_REAL_SENSOR = True
    print("✅ Sensor DHT11 detectado. Usando dados reais.")
except ImportError:
    print("⚠️ Biblioteca Adafruit_DHT não encontrada. Usando MOCK de sensor.")


def get_sensor_data():
    """Decide se retorna valores reais ou mock"""
    if USE_REAL_SENSOR:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        if humidity is not None and temperature is not None:
            return {
                "temperature": round(temperature, 1),
                "humidity": round(humidity, 1),
                "water_quality": 80  # exemplo fixo (ou de outro sensor real)
            }
        else:
            print("⚠️ Erro ao ler o sensor. Usando MOCK.")
    return mock_sensor()


@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(get_sensor_data())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
