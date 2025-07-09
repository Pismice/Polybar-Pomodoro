#!/usr/bin/env python3
import sqlite3
import os

db_file = "/home/tetratrux/.config/polybar/scripts/mybar_progress.db"

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()


# If at 30 minutes (1800 seconds), restart to 0, otherwise toggle paused status
cursor.execute("UPDATE progress SET seconds = 0 WHERE id = 1")
conn.commit()
print("Progress reseted")


conn.close()
