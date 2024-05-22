import sqlite3

database_path = "data/Car_Database.db"

conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Drop the alembic_version table
cursor.execute("DROP TABLE IF EXISTS alembic_version")

conn.commit()
conn.close()
