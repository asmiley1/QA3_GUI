import sqlite3
import sqlite3

def initialize_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Financial_Management (
                        id INTEGER PRIMARY KEY,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        correct_option TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Data_Analytics (
                        id INTEGER PRIMARY KEY,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        correct_option TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Database_Management (
                        id INTEGER PRIMARY KEY,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        correct_option TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Business_Application_Development (
                        id INTEGER PRIMARY KEY,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        correct_option TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Organizational_Management (
                        id INTEGER PRIMARY KEY,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        correct_option TEXT)''')

    conn.commit()
    conn.close()

def add_question_to_subject(database_name, subject, question, options, correct_option):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Insert the question and its options into the respective subject's table
    cursor.execute(f'''INSERT INTO {subject} 
                    (question, option_a, option_b, option_c, option_d, correct_option) 
                    VALUES (?, ?, ?, ?, ?, ?)''', (question, *options, correct_option))
    conn.commit()
    conn.close()

database_name = 'quiz.db'
initialize_database(database_name)