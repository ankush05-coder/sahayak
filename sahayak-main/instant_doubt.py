import sqlite3
from datetime import datetime
from google import genai
import json
GEMINI_API_KEY="AIzaSyDcZCLKTI10pj9KNmsn9TgTEQJcqO1K4Ck"
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=GEMINI_API_KEY)

contents="Generate a 200-word story in Marathi about a farmer learning about soil types (loamy, sandy, clay) for 5th-grade students."
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=contents
)



# Connect to SQLite DB (creates file if doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create a table to store prompts & responses
cursor.execute("""
CREATE TABLE IF NOT EXISTS llm_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT,
    response TEXT,
    timestamp TEXT
)
""")
# Insert into DB
cursor.execute("""
INSERT OR REPLACE INTO llm_logs (prompt, response, timestamp)
VALUES (?, ?, ?)
""", (contents, response.text, datetime.now().isoformat()))

conn.commit()
conn.close()

print("Saved LLM response to database.db")



