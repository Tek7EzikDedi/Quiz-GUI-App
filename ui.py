from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "italic"))
        self.score_label.grid(column=1, row=0)



        self.canvas = Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125,width=280, text="Some Question Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50,)


        self.checkmark = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.checkmark, bg=THEME_COLOR, highlightthickness=0, command=self.check_true_answer)
        self.true_button.grid(column=0, row=2)

        self.wrongmark = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.wrongmark, bg=THEME_COLOR, highlightthickness=0, command=self.check_false_answer)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def check_true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")


