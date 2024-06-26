import tkinter as tk
from tkinter import ttk
import sqlite3

class SelectSubjectApp:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback
        self.master.title("Select Subject")
        
        self.category_label = tk.Label(master, text="Select Category:", font=("Arial", 16))
        self.category_label.pack()

        # Connect to the database
        self.conn = sqlite3.connect('quiz.db')
        self.cursor = self.conn.cursor()
        self.available_tables = self.get_table_names()

        # Convert table names to Proper Case and remove underscores
        self.available_tables_proper = [self.to_proper_case(name) for name in self.available_tables]

        self.category_combobox = ttk.Combobox(master, values=self.available_tables_proper, font=("Arial", 14))
        self.category_combobox.pack()

        self.start_button = tk.Button(master, text="Start Quiz", command=self.start_quiz, font=("Arial", 14))
        self.start_button.pack()

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
        table_names = self.cursor.fetchall()
        return [table[0] for table in table_names]

    def to_proper_case(self, name):
        return name.replace('_', ' ').title()

    def start_quiz(self):
        category_proper = self.category_combobox.get()
        if category_proper:
            category = self.available_tables[self.available_tables_proper.index(category_proper)]

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
        self.correct_answers = 0
        self.wrong_answers = 0
        
        self.display_question()

    def fetch_questions(self):
        self.cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_option FROM {self.category};")
        return self.cursor.fetchall()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question, option_a, option_b, option_c, option_d, correct_option = self.questions[self.current_question_index]

            self.question_label = tk.Label(self, text=f"Question {self.current_question_index + 1}:\n{question}", font=("Arial", 14))
            self.question_label.pack()

            option_buttons = [
                ("A", option_a),
                ("B", option_b),
                ("C", option_c),
                ("D", option_d)
            ]

            self.selected_answer = tk.StringVar()  # Variable to store selected answer

            for letter, option in option_buttons:
                option_button = tk.Radiobutton(self, text=f"{letter}. {option}", variable=self.selected_answer, value=letter)
                option_button.pack(anchor='w')

            submit_button = tk.Button(self, text="Submit Answer", command=self.submit_answer, font=("Arial", 14))
            submit_button.pack(pady=10)
        else:
            self.display_end_message()

    def submit_answer(self):
        selected_answer = self.selected_answer.get()
        correct_option = self.questions[self.current_question_index][5]
        
        if selected_answer.upper() == correct_option.upper():
            self.correct_answers += 1
            feedback = "Correct!"
            color = "green"
        else:
            self.wrong_answers += 1
            feedback = "Sorry, better luck next time!"
            color = "red"
        
        feedback_label = tk.Label(self, text=feedback, fg=color, font=("Arial", 14))
        feedback_label.pack()

        self.current_question_index += 1

        next_button = tk.Button(self, text="Next", command=self.next_question, font=("Arial", 14))
        next_button.pack(pady=10)

    def next_question(self):
        self.clear_screen()
        self.display_question()

    def display_end_message(self):
        end_label = tk.Label(self, text="End of Quiz", font=("Arial", 16, "bold"))
        end_label.pack()

        total_label = tk.Label(self, text=f"Total Correct: {self.correct_answers}, Total Wrong: {self.wrong_answers}")
        total_label.pack()

        play_again_button = tk.Button(self, text="Play Again", command=self.play_again)
        play_again_button.pack()

    def play_again(self):
        self.destroy()  # Close the quiz window
        root.deiconify()  # Show the category selection window

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

def start_quiz(category):
    quiz_window = QuizGameApp(root, category)

def main():
    global root
    root = tk.Tk()
    app = SelectSubjectApp(root, start_quiz)
    root.mainloop()

if __name__ == "__main__":
    main()