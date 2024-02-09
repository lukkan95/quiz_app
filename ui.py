import tkinter as tk

HEME_COLOR = "#375362"
PATH_IMG_FALSE = "./images/false.png"
PATH_IMG_TRUE = "./images/true.png"


class QuizInterface(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Quiz")
        self.root.resizable(False, False)
        self.root.config(padx=20, pady=20, bg=HEME_COLOR)

        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0, width=300, height=300)
        self.canvas.grid(row=0, column=0, sticky="nsew", columnspan=3)

        self.button_false = self.add_button(PATH_IMG_FALSE, 1, 0, None)
        self.button_true = self.add_button(PATH_IMG_TRUE, 1, 2, None)


        self.root.mainloop()

    def add_button(self, img_path, row, column, command):
        button_img = tk.PhotoImage(file=img_path)
        button = tk.Button(self.root, image=button_img, command=lambda: command)
        button.image = button_img
        button.grid(row=row, column=column, padx=50, pady=50)
        return button




quiz = QuizInterface()