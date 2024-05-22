import sqlite3


def print_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for column in columns:
            print(f"  {column[1]} ({column[2]})")
        print()

    conn.close()


if __name__ == "__main__":
    db_path = r"C:\Users\Alon\OneDrive\Docs\Kozminski\4th semester\Python\project\flask-car-company\data\Car_Database.db"
    print_schema(db_path)
