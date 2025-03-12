from utilities.readfromglobalproperties import create_DB_connection


def test_db_connection():
    conn = create_DB_connection()
    
conn = test_db_connection()