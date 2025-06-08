import sqlite3
import json
from datetime import datetime
from config.settings import settings


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(settings.DB.NAME)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()

        #Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            language TEXT DEFAULT 'en',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        #Weather history table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            city TEXT,
            weather_data TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)

        self.conn.commit()

    async def add_user(self, user_id: int, username: str, first_name: str, last_name: str, language: str):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO users (user_id, username, first_name, last_name, language)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, first_name, last_name, language))
        self.conn.commit()

    async def get_user(self, user_id: int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            return {
                "user_id": row[0],
                "username": row[1],
                "first_name": row[2],
                "last_name": row[3],
                "language": row[4],
                "created_at": row[5]
            }
        return None

    async def update_user(self, user_id: int, updates: dict):
        cursor = self.conn.cursor()
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [user_id]
        cursor.execute(f"UPDATE users SET {set_clause} WHERE user_id = ?", values)
        self.conn.commit()

    async def add_weather_request(self, user_id: int, city: str, weather_data: str):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO weather_history (user_id, city, weather_data)
        VALUES (?, ?, ?)
        """, (user_id, city, weather_data))
        self.conn.commit()

    async def get_weather_history(self, user_id: int, limit: int = 5):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT city, timestamp FROM weather_history 
        WHERE user_id = ? 
        ORDER BY timestamp DESC 
        LIMIT ?
        """, (user_id, limit))
        return [{"city": row[0], "timestamp": row[1]} for row in cursor.fetchall()]

    def __del__(self):
        self.conn.close()