import sqlite3
from typing import List, Tuple
import os

# Update DB_PATH to point to the database in the 'data' directory
DB_PATH = os.path.join(os.path.dirname(__file__), "../..", "data", "fakedata.db")

def get_db_connection():
	"""Establish and return a connection to the SQLite database."""
	return sqlite3.connect(DB_PATH)

class FakeDataGenerator:
	def fetch_all_fake_data(self):
		"""Fetch all fake data from the SQLite database."""
		conn = get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM fake_data")
		rows = cursor.fetchall()
		conn.close()
		return rows

	def generate_fake_data(self):
		"""Fetch data dynamically from the SQLite database."""
		rows = self.fetch_all_fake_data()
		# Convert rows into a list of dictionaries
		return [
			{
				"name": row[0],
				"gender": row[1],
				"email": row[2],
				"address": row[3],
				"city": row[4],
				"job": row[5],
				"zipcode": row[6],
				"contact": row[7],
				"role": row[8],
				"company": row[9],
			}
			for row in rows
		]

	def fetch_all_fake_data(self):
		"""Fetch all fake data from the SQLite database."""
		conn = get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM fake_data")
		rows = cursor.fetchall()
		conn.close()
		return rows

	def fetch_fake_data_by_count(self, count: int):
		"""Fetch a specific number of fake data records from the SQLite database."""
		conn = get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM fake_data LIMIT ?", (count,))
		rows = cursor.fetchall()
		conn.close()
		return rows

	def generate_fake_data(self, count: int):
		"""Fetch data dynamically from the SQLite database based on the count."""
		rows = self.fetch_fake_data_by_count(count)
		# Convert rows into a list of dictionaries
		return [
			{
				"name": row[0],
				"gender": row[1],
				"email": row[2],
				"address": row[3],
				"city": row[4],
				"job": row[5],
				"zipcode": row[6],
				"contact": row[7],
				"role": row[8],
				"company": row[9],
			}
			for row in rows
		]