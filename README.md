# IoT Integration

A minimal Flask service for ingesting temperature readings from IoT sensors, backed by SQLite. Includes a mock sensor script for local testing.

## Components

- **`app.py`** — Flask API with two endpoints:
  - `POST /sensor-data` — accepts `{"device": string, "temp": number}`, validates the payload, and stores the reading.
  - `GET /temperature` — returns the 200 most recent readings, newest first.
- **`database.py`** — SQLite persistence layer (`sensor_data.db`), auto-creates the `readings` table on startup.
- **`mock_sensor.py`** — simulates a device (`sensor-mock-01`) posting a random temperature (18–26°C) to the API every 2 seconds.
- **`openapi.yaml`** — reserved for the API spec (not yet written).

## Getting started

```bash
python -m venv .venv
.venv/Scripts/activate   # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt

python app.py
```

The API starts on `http://localhost:5000`.

In a second terminal, run the mock sensor to start sending data:

```bash
python mock_sensor.py
```

## API

### `POST /sensor-data`

Request body:

```json
{
  "device": "sensor-mock-01",
  "temp": 21.5
}
```

Response:

```json
{ "status": "ok" }
```

Returns `400` if `device` or `temp` is missing, or if `temp` is not a number.

### `GET /temperature`

Returns the latest readings:

```json
[
  {
    "id": 42,
    "device": "sensor-mock-01",
    "temp": 21.5,
    "timestamp": "2026-08-11 12:34:56"
  }
]
```

## Status

Early-stage / work in progress.
