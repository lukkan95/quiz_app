import tkinter as tk
from quiz_brain import QuizBrain

HEME_COLOR = "#375362"
PATH_IMG_FALSE = "./images/false.png"
PATH_IMG_TRUE = "./images/true.png"
FONT_STYLE_1 = ("Ariel", 12, "italic")
FONT_STYLE_2 = ("Ariel", 12, "italic")


class QuizInterface(object):

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.root = tk.Tk()
        self.root.geometry("450x550")
        self.root.title("Quiz")
        self.root.resizable(False, False)
        self.root.config(padx=20, pady=20, bg=HEME_COLOR)

        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0, width=300, height=300)
        self.canvas_text = self.canvas.create_text(200, 150, text="Some text", font=FONT_STYLE_1, width=300)
        self.canvas.grid(row=1, column=0, sticky="nsew", columnspan=3)

        self.score_label = tk.Label(self.root, text=f"Score: 0", font=FONT_STYLE_2, padx=5, pady=5, bg=HEME_COLOR)
        self.score_label.grid(row=0, column=2)

        self.button_false = self.add_button(PATH_IMG_FALSE, row=2, column=0, command=lambda: (self.check_answer("False")))
        self.button_true = self.add_button(PATH_IMG_TRUE, row=2, column=2, command=lambda: (self.check_answer("True")))

        self.change_canvas_text()

        self.root.mainloop()

    def check_answer(self, answer):
        check = self.quiz_brain.check_answer(answer)
        self.change_score()
        if check:
            self.canvas.configure(bg="green")

        else:
            self.canvas.configure(bg="red")
        self.root.after(1000, self.change_canvas_text)

    def change_score(self):
        self.score_label.configure(text=f"Score: {self.quiz_brain.score}")
        self.score_label.update()

    def change_canvas_text(self):
        self.canvas.configure(bg="white")
        if self.quiz_brain.still_has_questions():
            text = self.quiz_brain.next_question()
            self.canvas.itemconfigure(self.canvas_text, text=text)
        else:
            self.button_true.configure(state="disabled")
            self.button_false.configure(state="disabled")
            self.canvas.itemconfigure(self.canvas_text, text=f"You've completed the quiz\nYour final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}")

    def add_button(self, img_path, row, column, command):
        button_img = tk.PhotoImage(file=img_path)
        button = tk.Button(self.root, image=button_img, command=command)
        button.image = button_img
        button.grid(row=row, column=column, padx=50, pady=50)
        return button



