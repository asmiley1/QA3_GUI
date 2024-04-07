import tkinter as tk
from tkinter import ttk
import sqlite3

class SelectSubjectApp:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback
        self.master.title("Select Subject")
        
        self.category_label = tk.Label(master, text="Select Category:")
        self.category_label.pack()

        # Connect to the database
        self.conn = sqlite3.connect('quiz.db')
        self.cursor = self.conn.cursor()
        self.available_tables = self.get_table_names()

        self.category_combobox = ttk.Combobox(master, values=self.available_tables)
        self.category_combobox.pack()

        self.start_button = tk.Button(master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
        table_names = self.cursor.fetchall()
        return [table[0] for table in table_names]

    def start_quiz(self):
        category = self.category_combobox.get()
        if category:
            self.master.withdraw()  # Hide category selection window
            self.callback(category)

class QuizGameApp(tk.Toplevel):
    def __init__(self, master, category):
        super().__init__(master)
        self.title("Quiz")
        self.category = category
        
        # Connect to the database
        self.conn = sqlite3.connect('quiz.db')
        self.cursor = self.conn.cursor()
        
        self.questions = self.fetch_questions()
        self.current_question_index = 0
        
        self.display_question()

    def fetch_questions(self):
        self.cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_option FROM {self.category} LIMIT 10;")
        return self.cursor.fetchall()

    def display_question(self):
        question, option_a, option_b, option_c, option_d, correct_option = self.questions[self.current_question_index]
        
        question_label = tk.Label(self, text=f"Question {self.current_question_index + 1}: {question}")
        question_label.pack()

        option_buttons = [
            ("A", option_a),
            ("B", option_b),
            ("C", option_c),
            ("D", option_d)
        ]

        for letter, option in option_buttons:
            option_button = tk.Button(self, text=f"{letter}. {option}", command=lambda ans=letter: self.check_answer(ans, correct_option))
            option_button.pack()

    def check_answer(self, selected_answer, correct_answer):
        if selected_answer.upper() == correct_answer.upper():
            feedback = "Congrats!"
            color = "green"
        else:
            feedback = "Sorry, better luck next time!"
            color = "red"
        
        feedback_label = tk.Label(self, text=feedback, fg=color)
        feedback_label.pack()

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.display_end_message()

    def display_end_message(self):
        end_label = tk.Label(self, text="End of Quiz")
        end_label.pack()

        select_another_button = tk.Button(self, text="Select Another Category", command=self.select_another_category)
        select_another_button.pack()

    def select_another_category(self):
        self.destroy()  # Close the quiz window
        root.deiconify()  # Show the category selection window

def start_quiz(category):
    quiz_window = QuizGameApp(root, category)

def main():
    global root
    root = tk.Tk()
    app = SelectSubjectApp(root, start_quiz)
    root.mainloop()

if __name__ == "__main__":
    main()