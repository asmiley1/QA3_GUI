# QA3_GUI
Quarterly Assessment Three GUI


- main.py

Importing Libraries: The script begins by importing the necessary libraries, including tkinter for the GUI, sqlite3 for database operations, and ttk for themed widgets in tkinter.

SelectSubjectApp Class: This class represents the GUI window where the user selects a subject category. It initializes the window, connects to the database, retrieves the available table names, creates a combobox with the table names, and provides a button to start the quiz.

QuizGameApp Class: This class represents the quiz window. It inherits from tk.Toplevel, indicating it's a separate window from the main application. Upon initialization, it connects to the database, fetches questions for the selected category, and initializes variables to track user progress. It displays questions one by one and handles user input for answers.

QuizDatabase Class: This class encapsulates database operations. It connects to the database upon initialization and provides methods to retrieve table names and questions for a specific category.

start_quiz Function: This function is the callback function passed to the SelectSubjectApp class. It initializes the QuizGameApp window when the user selects a category.

main Function: This is the entry point of the script. It creates the main tkinter window (root), initializes the SelectSubjectApp, and starts the main event loop.