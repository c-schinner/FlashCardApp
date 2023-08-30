from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# The Functions for the buttons
def x_mark():
    global current_card, start_timer
    window.after_cancel(start_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=photo_front_card)
    canvas.itemconfig(language_name, text="French", fill="black")
    canvas.itemconfig(language_text, text=current_card["French"], fill="black")
    start_timer = window.after(3000, flip_card)


def check_mark():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    x_mark()


def flip_card():
    canvas.itemconfig(card_background, image=photo_back_card)
    canvas.itemconfig(language_name, text="English", fill="white")
    canvas.itemconfig(language_text, text=current_card["English"], fill="white")


# Window and Canvas setup and placement with the images in place #
window = Tk()
window.title("Flash Card Fun!")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

start_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
photo_front_card = PhotoImage(file="./images/card_front.png")
photo_back_card = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=photo_front_card)
canvas.config(bg=BACKGROUND_COLOR)
language_name = canvas.create_text(400, 100, text="", fill="black", font=("Ariel", 20, "italic"))
language_text = canvas.create_text(400, 275, text="", fill="black", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# The Buttons setup and placement #
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")

correct = Button(image=correct_image, highlightthickness=0, command=check_mark)
correct.config(padx=50)
correct.grid(row=1, column=0)

incorrect = Button(image=incorrect_image, highlightthickness=0, command=x_mark)
incorrect.config(padx=50)
incorrect.grid(row=1, column=1)

check_mark()

window.mainloop()
