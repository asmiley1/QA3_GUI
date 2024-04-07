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

        
        self.database_name = 'quiz.db'
        self.quiz_database = QuizDatabase(self.database_name)
        self.available_tables_proper = [self.to_proper_case(name) for name in self.quiz_database.get_table_names()]
        
        self.category_combobox = ttk.Combobox(master, values=self.available_tables_proper, font=("Arial", 14))
        self.category_combobox.pack()

        self.start_button = tk.Button(master, text="Start Quiz", command=self.start_quiz, font=("Arial", 14))
        self.start_button.pack()

    def to_proper_case(self, name):
        return name.replace('_', ' ').title()

    def start_quiz(self):
        category_proper = self.category_combobox.get()
        if category_proper:
            category = self.available_tables_proper[self.available_tables_proper.index(category_proper)]

            self.master.withdraw() 
            self.callback(category, self.database_name)

class QuizGameApp(tk.Toplevel):
    def __init__(self, master, category, database_name):
        super().__init__(master)
        self.title("Quiz")
        self.category = category
        self.database_name = database_name
        
        
        self.quiz_database = QuizDatabase(self.database_name)
        
        self.questions = self.quiz_database.get_questions(self.category)
        self.current_question_index = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        
        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question, options, correct_option = self.questions[self.current_question_index]

            question_label = tk.Label(self, text=f"Question {self.current_question_index + 1}:\n{question}", font=("Arial", 14))
            question_label.pack()

            option_buttons = [
                ("A", options[0]),
                ("B", options[1]),
                ("C", options[2]),
                ("D", options[3])
            ]

            for letter, option in option_buttons:
                option_button = tk.Button(self, text=f"{letter}. {option}", command=lambda ans=letter: self.check_answer(ans, correct_option), width=50, wraplength=300)
                option_button.pack(pady=5)

            next_button = tk.Button(self, text="Next", command=self.next_question, font=("Arial", 14))
            next_button.pack(pady=10)
        else:
            self.display_end_message()

    def next_question(self):
        self.current_question_index += 1
        self.clear_screen()
        self.display_question()

    def check_answer(self, selected_answer, correct_answer):
        if selected_answer.upper() == correct_answer.upper():
            self.correct_answers += 1
            feedback = "Correct!"
            color = "green"
        else:
            self.wrong_answers += 1
            feedback = "Sorry, better luck next time!"
            color = "red"
        
        feedback_label = tk.Label(self, text=feedback, fg=color, font=("Arial", 14))
        feedback_label.pack()

    def display_end_message(self):
        end_label = tk.Label(self, text="End of Quiz", font=("Arial", 16, "bold"))
        end_label.pack()

        total_label = tk.Label(self, text=f"Total Correct: {self.correct_answers}, Total Wrong: {self.wrong_answers}")
        total_label.pack()

        play_again_button = tk.Button(self, text="Play Again", command=self.play_again)
        play_again_button.pack()

    def play_again(self):
        self.destroy()  
        root.deiconify()  

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

class QuizDatabase:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
        table_names = self.cursor.fetchall()
        return [table[0] for table in table_names]

    def get_questions(self, category):
        self.cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_option FROM {category.replace(' ', '_').lower()};")
        questions = []
        for row in self.cursor.fetchall():
            question, options, correct_option = row[0], row[1:5], row[5]
            questions.append((question, options, correct_option))
        return questions

def start_quiz(category, database_name):
    quiz_window = QuizGameApp(root, category, database_name)

def main():
    global root
    root = tk.Tk()
    app = SelectSubjectApp(root, start_quiz)
    root.mainloop()

if __name__ == "__main__":
    main()