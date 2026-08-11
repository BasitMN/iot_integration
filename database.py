import sqlite3

def get_conn():
    conn = sqlite3.connect('sensor_data.db')
    conn.row_factory = sqlite3.Row   # gör att raderna kan bli dictionaries
    return conn

def init_db():
    conn = get_conn()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device TEXT NOT NULL,
            temp REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_reading(device, temp):
    conn = get_conn()
    conn.execute('INSERT INTO readings (device, temp) VALUES (?, ?)', (device, temp))
    conn.commit()
    conn.close()

def get_readings():
    conn = get_conn()
    rows = conn.execute('SELECT * FROM readings ORDER BY id DESC LIMIT 200').fetchall()
    conn.close()
    return [dict(r) for r in rows]