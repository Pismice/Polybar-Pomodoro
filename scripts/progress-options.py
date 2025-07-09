#!/usr/bin/env python3
import sqlite3
import os

db_file = "/home/tetratrux/.config/polybar/scripts/mybar_progress.db"

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Read current paused status
cursor.execute("SELECT seconds, paused FROM progress WHERE id = 1")
result = cursor.fetchone()
if result:
    current_seconds, current_paused = result
else:
    current_seconds, current_paused = 0, True

# If at 30 minutes (1800 seconds), restart to 0, otherwise toggle paused status
if current_seconds >= 1800:
    cursor.execute("UPDATE progress SET seconds = 0, paused = 0 WHERE id = 1")
    conn.commit()
    print("Progress restarted")
else:
    # Toggle paused status
    new_paused = not current_paused
    cursor.execute("UPDATE progress SET paused = ? WHERE id = 1", (new_paused,))
    conn.commit()
    status = "paused" if new_paused else "running"
    print(f"Progress {status}")

conn.close()
