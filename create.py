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

questions = {
    'Financial_Management': [
        ("What does ROI stand for?", ["Return on Investment", "Return on Income", "Revenue of Interest", "Revenue on Investment"], "A"),
        ("What is a balance sheet used for?", ["Tracking income and expenses", "Assessing financial health", "Managing employees", "Forecasting sales"], "B"),
        
    ],
    'Data_Analytics': [
        ("What is data visualization used for?", ["Storing data", "Presenting data in graphical form", "Analyzing data", "Collecting data"], "B"),
        ("What is clustering in data analysis?", ["Sorting data into groups with similar characteristics", "Calculating averages", "Filtering out irrelevant data", "Identifying outliers"], "A"),
        
    ],
    'Database_Management': [
        ("What is a primary key in a database?", ["A unique identifier for a record", "A foreign key", "A required field", "A secondary index"], "A"),
        ("What is normalization in database design?", ["Storing data in multiple formats", "Reducing redundancy and improving efficiency", "Adding redundant data", "Combining multiple tables into one"], "B"),
        
    ],
    'Business_Application_Development': [
        ("What is an API?", ["An application programming interface", "An application for data analysis", "A software development tool", "A database management system"], "A"),
        ("What is the purpose of version control systems?", ["Tracking changes to code", "Managing databases", "Creating backups", "Writing documentation"], "A"),
        
    ],
    'Organizational_Management': [
        ("What is the role of organizational culture?", ["Defining company values and behaviors", "Managing finances", "Hiring employees", "Writing policies and procedures"], "A"),
        ("What is the purpose of performance appraisals?", ["Setting employee salaries", "Evaluating employee performance", "Training employees", "Promoting employees"], "B"),
    ],
}

for subject, question_list in questions.items():
    for question, options, correct_option in question_list:
        add_question_to_subject(database_name, subject, question, options, correct_option)

print("Questions added successfully.")