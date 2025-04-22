import sqlite3
from typing import List, Tuple

DB_PATH = "fakedata.db"  # Path to your SQLite database file

def get_db_connection():
	"""Establish and return a connection to the SQLite database."""
	return sqlite3.connect(DB_PATH)

def fetch_all_fake_data() -> List[Tuple]:
	"""Fetch all rows from the fake_data table."""
	connection = get_db_connection()
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT * FROM fake_data")
		rows = cursor.fetchall()
		return rows
	finally:
		connection.close()