THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Skibidi Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score = self.quiz.score
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # To wrap text within the canvas
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # True Buttons
        right_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_img, highlightthickness=0, command=self.left)
        self.right_btn.grid(row=2, column=0, pady=20)

        # False Button
        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_img, highlightthickness=0, command=self.right)
        self.wrong_btn.grid(row=2, column=1, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\nFinal Score: {self.quiz.score}/{self.quiz.question_number}")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def left(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def right(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_label.config(text=f"Score: {self.quiz.score}")


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)