import requests, time, random

API_URL = "http://localhost:5000/sensor-data"
DEVICE_ID = "sensor-mock-01"

def run_sensor():
    print(f"Startar mock-sensor: {DEVICE_ID}")
    while True:
        payload = {
            "device": DEVICE_ID,
            "temp": round(random.uniform(18.0, 26.0), 2)
        }
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                print(f"Skickat: {payload['temp']}°C - Status: {response.json()['status']}")
            else:
                print(f"Fel vid sändning: {response.status_code}")
        except Exception as e:
            print(f"Kunde inte kontakta API:et: {e}")
        time.sleep(2)

if __name__ == '__main__':
    run_sensor()