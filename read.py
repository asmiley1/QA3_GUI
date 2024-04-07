import sqlite3

def read_database(database_file):
    try:
        
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            print(f"Table: {table_name}")
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error reading database: {e}")


read_database('quiz.db')