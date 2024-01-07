THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

import tkinter as tk

class QuizInterface():

    def __init__(self):
        # Initialize Attributes
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR, foreground="white", font=("Arial", 10, "bold"))
        self.lbl_score.grid(column=1, row=0, padx=20, pady=20)

        self.cnv_q = tk.Canvas(width=300, height=250)
        self.question_shown = self.cvn_q.create_text(150, 125, text="Questions here", font=FONT)
        self.cnv_q.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        img_true = tk.PhotoImage(file="Quiz_App/images/true.png")
        img_false = tk.PhotoImage(file="Quiz_App/images/false.png")

        self.btn_true = tk.Button(image=img_true, highlightthickness=0, command=self.true_submit)
        self.btn_true.grid(column=0, row=2, padx=20, pady=20)

        self.btn_false = tk.Button(image=img_false, highlightthickness=0, command=self.false_submit)
        self.btn_false.grid(column=1, row=2, padx=20, pady=20)

        self.window.mainloop()

    def update_score(self):
        self.score += 1
        self.lbl_score.config(text=f"Score: {self.score}")

    def update_question(self, question):
        self.cnv_q.itemconfig(self.question_shown, text=f"{question}")

    def true_submit(self):
        pass

    def false_submit(self):
        pass