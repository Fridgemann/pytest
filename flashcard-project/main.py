from tkinter import *
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
after_handle = 1


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data_dict = pd.DataFrame.to_dict(data)

fr_list = []
en_list = []

for n in data_dict["French"]:
    fr_list.append(data_dict["French"][n])

for n in data_dict["English"]:
    en_list.append(data_dict["English"][n])


def get_word():
    global fr_word, en_word
    random_index = rand.randint(0, len(fr_list) - 1)
    fr_word = fr_list[random_index]
    en_word = en_list[random_index]


def create_word():
    if after_handle:
        window.after_cancel(after_handle)
    global image, language, word
    get_word()
    image = screen.create_image(0, 0, anchor=NW, image=card_front)
    language = screen.create_text(400, 50, text="French", font=("Ariel", 40, "italic"), fill="black")
    word = screen.create_text(400, 263, text=fr_word, font=("Ariel", 60, "bold"), fill="black")
    window.after(3000, func=flip_card)



def flip_card():
    screen.itemconfig(image, image=card_back)
    screen.itemconfig(language, text="English")
    screen.itemconfig(word, text= en_word)



def word_is_known():
    en_list.remove(en_word)
    fr_list.remove(fr_word)
    words_to_learn_dict = {
        "French": fr_list,
        "English": en_list
    }
    dataframe = pd.DataFrame(words_to_learn_dict)
    dataframe.to_csv("data/words_to_learn.csv", index=False)
    if after_handle:
        window.after_cancel(after_handle)
    global image, language, word
    get_word()
    image = screen.create_image(0, 0, anchor=NW, image=card_front)
    language = screen.create_text(400, 50, text="French", font=("Ariel", 40, "italic"), fill="black")
    word = screen.create_text(400, 263, text=fr_word, font=("Ariel", 60, "bold"), fill="black")
    window.after(3000, func=flip_card)





window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

screen = Canvas(bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=word_is_known)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=create_word)

screen.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)


create_word()

after_handle = window.after(3000, func=flip_card)



window.mainloop()


