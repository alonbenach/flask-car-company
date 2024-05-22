import sqlite3

database_path = "data/Car_Database.db"

conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Drop all tables (be careful with this in production)
cursor.executescript(
    """
    DROP TABLE IF EXISTS Customers;
    DROP TABLE IF EXISTS Customer_Ownership;
    DROP TABLE IF EXISTS Car_Vins;
    DROP TABLE IF EXISTS Car_Options;
    DROP TABLE IF EXISTS Car_Parts;
    DROP TABLE IF EXISTS Brands;
    DROP TABLE IF EXISTS Dealers;
    DROP TABLE IF EXISTS Dealer_Brand;
    DROP TABLE IF EXISTS Manufacture_Plant;
    DROP TABLE IF EXISTS Engines;
"""
)
conn.commit()
conn.close()
