#!/usr/bin/env python3
import sqlite3
import os

db_file = "/home/tetratrux/.config/polybar/scripts/mybar_progress.db"

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS progress 
                 (id INTEGER PRIMARY KEY, seconds INTEGER, paused BOOLEAN DEFAULT 1)''')

# Read progress and paused status
cursor.execute("SELECT seconds, paused FROM progress WHERE id = 1")
result = cursor.fetchone()
if result:
    seconds, paused = result
else:
    seconds, paused = 0, True
    cursor.execute("INSERT INTO progress (id, seconds, paused) VALUES (1, ?, ?)", (seconds, paused))
    conn.commit()

# Increment seconds if not at 30 minutes (1800 seconds) and not paused
if seconds < 1800 and not paused:
    seconds += 1
    cursor.execute("UPDATE progress SET seconds = ? WHERE id = 1", (seconds,))
    conn.commit()

# Convert seconds to minutes and seconds
minutes = seconds // 60
remaining_seconds = seconds % 60

# Draw progress bar (30 blocks for 30 minutes)
blocks = int(seconds / 60)  # One block per minute
filled_blocks = "█" * blocks
empty_blocks = "░" * (30 - blocks)
bar = f"%{{F#0088ff}}{filled_blocks}%{{F-}}{empty_blocks}"

if paused:
    print(f"{bar} {minutes:02d}:{remaining_seconds:02d} paused")
else:
    print(f"{bar} {minutes:02d}:{remaining_seconds:02d} working ...")

conn.close()