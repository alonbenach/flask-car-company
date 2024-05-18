import sqlite3


def clear_alembic_version(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear the alembic_version table
    cursor.execute("DELETE FROM alembic_version;")
    conn.commit()

    cursor.execute("SELECT * FROM alembic_version;")
    rows = cursor.fetchall()

    if not rows:
        print("Successfully cleared the alembic_version table.")
    else:
        print("Failed to clear the alembic_version table.")

    conn.close()


if __name__ == "__main__":
    db_path = "data/Car_Database.db"  # Adjust this path if necessary
    clear_alembic_version(db_path)
