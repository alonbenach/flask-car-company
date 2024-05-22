import sqlite3

# Path to your SQLite database
database_path = "data/Car_Database.db"
# Path to your SQL file
sql_file_path = "data/Insert.sql"

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Read the SQL file
with open(sql_file_path, "r") as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script with error handling
try:
    cursor.executescript(sql_script)
    conn.commit()
    print("Data loaded successfully.")
except sqlite3.IntegrityError as e:
    print(f"SQLite Integrity Error: {e}")
    # You can also log the error or handle it in other ways here

# Close the connection
conn.close()
