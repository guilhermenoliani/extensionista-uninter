# backend/sensor.py
import random

def read_sensor():
    """Retorna valores simulados de temperatura, umidade e qualidade da água"""
    temperature = round(random.uniform(20, 30), 1)   # entre 20°C e 30°C
    humidity = round(random.uniform(40, 70), 1)      # entre 40% e 70%
    water_quality = random.randint(0, 100)           # 0 a 100%

    return {
        "temperature": temperature,
        "humidity": humidity,
        "water_quality": water_quality
    }
