import sqlite3
class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def to_tuple(self):
        return (self.question, *self.options, self.correct_option)

class QuizDatabase:
    def __init__(self, database_name):
        self.database_name = database_name
        self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        subjects = [
            'Financial_Management',
            'Data_Analytics',
            'Database_Management',
            'Business_Application_Development',
            'Organizational_Management'
        ]

        for subject in subjects:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {subject} (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                option_a TEXT,
                                option_b TEXT,
                                option_c TEXT,
                                option_d TEXT,
                                correct_option TEXT)''')

        conn.commit()
        conn.close()

    def add_question_to_subject(self, subject, question):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute(f'''INSERT INTO {subject} 
                        (question, option_a, option_b, option_c, option_d, correct_option) 
                        VALUES (?, ?, ?, ?, ?, ?)''', question.to_tuple())
        conn.commit()
        conn.close()

# Define questions
questions = {
    'Financial_Management': [
        Question("What does ROI stand for?", ["Return on Investment", "Return on Income", "Revenue of Interest", "Revenue on Investment"], "A"),
        Question("What is a balance sheet used for?", ["Tracking income and expenses", "Assessing financial health", "Managing employees", "Forecasting sales"], "B"),
        Question("What is the purpose of financial statements?", ["Providing information about the financial position", "Managing employees", "Developing marketing strategies", "Forecasting sales"], "A"),
        Question("What is the difference between fixed and variable costs?", ["Fixed costs remain constant, variable costs change with production levels", "Variable costs remain constant, fixed costs change with production levels", "Fixed costs are associated with production, variable costs are not", "Variable costs are associated with production, fixed costs are not"], "A"),
        Question("What is cash flow?", ["The total amount of money a business has", "The total amount of money owed to a business","The movement of money in and out of a business", "The total amount of money owed by a business"], "C"),
        Question("What is the purpose of financial ratios?", ["Assessing financial performance and health", "Managing employees", "Developing marketing strategies", "Forecasting sales"], "A"),
        Question("What is the formula for calculating gross profit?", [ "Total expenses minus total revenue", "Net profit divided by revenue", "Cost of goods sold divided by revenue","Revenue minus cost of goods sold"], "D"),
        Question("What is the difference between a budget and a forecast?", ["A budget is a plan for future expenses, a forecast is a prediction of future financial outcomes", "A forecast is a plan for future expenses, a budget is a prediction of future financial outcomes", "A budget is based on past performance, a forecast is based on future expectations", "A forecast is based on past performance, a budget is based on future expectations"], "A"),
        Question("What is the purpose of working capital management?", [ "To invest excess cash in long-term assets","To ensure the company has enough liquidity to meet its short-term obligations", "To minimize taxes", "To increase shareholder wealth"], "B"),
        Question("What is the time value of money?", ["The concept that money available today is worth more than the same amount in the future", "The concept that money available in the future is worth more than the same amount today", "The concept that money has no value over time", "The concept that money grows at a constant rate over time"], "A")
    ],
    'Data_Analytics': [
        Question("What is data visualization used for?", ["Storing data", "Presenting data in graphical form", "Analyzing data", "Collecting data"], "B"),
        Question("What is clustering in data analysis?", ["Sorting data into groups with similar characteristics", "Calculating averages", "Filtering out irrelevant data", "Identifying outliers"], "A"),
        Question("What is logistic regression used for?", ["Classification problems", "Clustering analysis", "Regression analysis", "Time series analysis"], "A"),
        Question("What is the purpose of data aggregation?", ["Combining data into summary statistics", "Identifying outliers", "Cleaning data", "Creating visualizations"], "A"),
        Question("What is the main goal of cluster analysis?", ["Grouping similar data points together", "Fitting a line to data points", "Predicting future values", "Analyzing time series data"], "A"),
        Question("What does the term 'outlier' refer to in data analysis?", ["An observation that deviates significantly from other observations", "An average observation", "A normal observation", "A data point with missing values"], "A"),
        Question("What is the difference between correlation and causation?", ["Correlation implies a relationship between variables, while causation implies that one variable directly influences another", "There is no difference", "Correlation refers to time-series data, while causation refers to cross-sectional data", "Causation implies a relationship between variables, while correlation implies that one variable directly influences another"], "A"),
        Question("What is the purpose of data normalization?", ["Scaling numerical features to a standard range", "Creating new variables", "Removing outliers", "Imputing missing values"], "A"),
        Question("What is a decision tree used for in data analysis?", ["Classification and regression", "Data aggregation", "Outlier detection", "Dimensionality reduction"], "A"),
        Question("What is the primary objective of exploratory data analysis?", ["To understand the main characteristics of the data", "To fit a model to the data", "To make predictions", "To validate a hypothesis"], "A")
    ],
    'Database_Management': [
        Question("What is a primary key in a database?", ["A unique identifier for a record", "A foreign key", "A required field", "A secondary index"], "A"),
        Question("What is normalization in database design?", ["Storing data in multiple formats", "Reducing redundancy and improving efficiency", "Adding redundant data", "Combining multiple tables into one"], "B"),
        Question("What is denormalization in database design?", ["Storing redundant data to improve performance", "Organizing data to minimize redundancy and dependency", "Combining multiple tables into one", "Adding redundant data"], "A"),
        Question("What is a composite key in a database?", ["A key composed of multiple columns", "A foreign key", "A primary key", "An index created for performance"], "A"),
        Question("What is the purpose of a database view?", ["To present data in a virtual table", "To store temporary data", "To improve query performance", "To link tables together"], "A"),
        Question("What is a database trigger?", ["A stored procedure that is automatically executed in response to certain events", "A table containing metadata about the database", "A method of data encryption", "A process that deletes outdated records"], "A"),
        Question("What is the difference between a relational and non-relational database?", ["Relational databases organize data into tables with rows and columns, while non-relational databases use other structures like documents or key-value pairs", "There is no difference", "Relational databases are faster than non-relational databases", "Non-relational databases are only used for small datasets"], "A"),
        Question("What is the purpose of database indexing?", ["To improve query performance by facilitating efficient data retrieval", "To organize data into tables with rows and columns", "To link tables together", "To prevent data redundancy"], "A"),
        Question("What is a database schema?", ["The structure that defines the organization of data in a database", "A precompiled collection of SQL statements", "A table that stores temporary data", "An index used for performance tuning"], "A"),
        Question("What is the purpose of database replication?", ["To create and maintain multiple copies of the same database", "To store redundant data", "To organize data to minimize redundancy and dependency", "To prevent unauthorized access to data"], "A")
    ],
    'Business_Application_Development': [
        Question("What is an API?", ["An application programming interface", "An application for data analysis", "A software development tool", "A database management system"], "A"),
        Question("What is the purpose of version control systems?", ["Tracking changes to code", "Managing databases", "Creating backups", "Writing documentation"], "A"),
        Question("What is MVC architecture in software development?", ["Model-View-Controller", "Model-View-Component", "Model-View-Container", "Model-View-Coordinator"], "A"),
        Question("What is the purpose of dependency injection in software development?", ["To achieve loose coupling between components", "To increase code duplication", "To reduce code complexity", "To improve code readability"], "A"),
        Question("What is the difference between REST and SOAP APIs?", ["REST APIs use HTTP protocols and are lightweight, SOAP APIs use XML and can be more complex", "There is no difference", "SOAP APIs use HTTP protocols and are lightweight, REST APIs use XML and can be more complex", "REST APIs are only used for simple data retrieval, SOAP APIs are used for complex operations"], "A"),
        Question("What is the primary benefit of microservices architecture?", ["Scalability and flexibility", "Security and performance", "Code maintainability", "Code reusability"], "A"),
        Question("What is the purpose of containerization in software software development?", ["To package applications and their dependencies together for easy deployment", "To improve user interface design", "To analyze market trends", "To create automated tests for software applications"], "A"),
        Question("What is the primary advantage of using cloud computing for application development?", ["Scalability and flexibility", "Security and performance", "Code maintainability", "Code reusability"], "A"),
        Question("What is the purpose of continuous deployment in software development?", ["To automate the process of deploying code changes to production servers", "To validate user interface design", "To analyze market trends", "To create automated tests for software applications"], "A")
    ],
    'Organizational_Management': [
        Question("What is the role of organizational culture?", ["Defining company values and behaviors", "Managing finances", "Hiring employees", "Writing policies and procedures"], "A"),
        Question("What is the purpose of performance appraisals?", ["Setting employee salaries", "Evaluating employee performance", "Training employees", "Promoting employees"], "B"),
        Question("What is organizational culture?", ["The shared values, beliefs, and practices within an organization", "The physical layout of the office space", "The organizational structure", "The financial performance of the organization"], "A"),
        Question("What is the purpose of strategic planning in organizational management?", ["To set long-term goals and objectives", "To manage day-to-day operations", "To hire new employees", "To increase shareholder wealth"], "A"),
        Question("What is the difference between leadership and management?", ["Leadership focuses on inspiring and motivating others, while management focuses on planning and organizing", "There is no difference", "Leadership involves day-to-day operations, while management involves long-term strategy", "Management focuses on inspiring and motivating others, while leadership focuses on planning and organizing"], "A"),
        Question("What is organizational structure?", ["The framework that defines the hierarchy and reporting relationships within an organization", "The physical layout of the office space", "The organizational culture", "The financial performance of the organization"], "A"),
        Question("What is change management?", ["The process of planning, implementing, and monitoring changes within an organization", "The process of hiring new employees", "The process of evaluating employee performance", "The process of setting strategic goals"], "A"),
        Question("What is the purpose of organizational communication?", ["To facilitate the flow of information within an organization", "To manage day-to-day operations", "To increase shareholder wealth", "To set long-term goals and objectives"], "A"),
        Question("What is the role of organizational behavior in management?", ["To understand and manage individual and group dynamics within an organization", "To set strategic goals", "To hire new employees", "To evaluate financial performance"], "A"),
        Question("What is the importance of diversity and inclusion in organizational management?", ["To create a more innovative and inclusive work environment", "To increase shareholder wealth", "To set long-term goals and objectives", "To manage day-to-day operations"], "A")
    ],
}

database_name = 'quiz.db'

quiz_database = QuizDatabase(database_name)

for subject, question_list in questions.items():
    for question in question_list:
        quiz_database.add_question_to_subject(subject, question)

print("Questions added successfully.")