from tkinter import *
from random import shuffle

FONT = "times new roman"
deck_array = []

root = Tk()
root.title("Clash Royale Deck System")
root.geometry("400x1000")

title_label = Label(root, text="Clash Royale Deck System")
title_label.config(font=(FONT, 24))
title_label.pack()

deck_creation_frame = Frame(root)

create_deck_label = Label(deck_creation_frame, text="Decklist")
create_deck_label.config(font=(FONT, 18))
create_deck_label.grid(row=0, column=0, columnspan=2)

entry_label = Label(deck_creation_frame, text="Enter 8 cards, space separated (remove spaces from card name)")
entry_label.config(font=(FONT, 11))
entry_label.grid(row=1)

entry = Entry(deck_creation_frame)
entry.config(font=(FONT, 11))
entry.grid(row=1, column=1)

submit_button = Button(deck_creation_frame, text="Submit Deck", command=lambda: begin_cycle(entry))
submit_button.config(font=(FONT, 11))
submit_button.grid(row=2)


def use_card(card_used, label):
    global deck_array

    if card_used == 1:
        temp = deck_array[0]

        deck_array[0] = deck_array[4]
        deck_array.pop(4)
        deck_array.append(temp)

        label["text"] = deck_array[0]
    elif card_used == 2:
        temp = deck_array[1]

        deck_array[1] = deck_array[4]
        deck_array.pop(4)
        deck_array.append(temp)

        label["text"] = deck_array[1]
    elif card_used == 3:
        temp = deck_array[2]

        deck_array[2] = deck_array[4]
        deck_array.pop(4)
        deck_array.append(temp)

        label["text"] = deck_array[2]
    elif card_used == 4:
        temp = deck_array[3]

        deck_array[3] = deck_array[4]
        deck_array.pop(4)
        deck_array.append(temp)

        label["text"] = deck_array[3]


def begin_cycle(entry_widget):
    global deck_array

    deck = entry_widget.get()
    deck_array = deck.split()
    shuffle(deck_array)

    card_1_frame = Frame(root)

    card_1_name_label = Label(card_1_frame, text=deck_array[0])
    card_1_name_label.config(font=(FONT, 11))
    card_1_name_label.pack()

    use1_button = Button(card_1_frame,text="Use Card", command=lambda:use_card(1, card_1_name_label))
    use1_button.config(font=(FONT, 11))
    use1_button.pack()

    card_1_frame.pack()

    card_2_frame = Frame(root)

    card_2_name_label = Label(card_2_frame, text=deck_array[1])
    card_2_name_label.config(font=(FONT, 11))
    card_2_name_label.pack()

    use2_button = Button(card_2_frame, text="Use Card", command=lambda: use_card(2, card_2_name_label))
    use2_button.config(font=(FONT, 11))
    use2_button.pack()

    card_2_frame.pack()

    card_3_frame = Frame(root)

    card_3_name_label = Label(card_3_frame, text=deck_array[2])
    card_3_name_label.config(font=(FONT, 11))
    card_3_name_label.pack()

    use3_button = Button(card_3_frame, text="Use Card", command=lambda: use_card(3, card_3_name_label))
    use3_button.config(font=(FONT, 11))
    use3_button.pack()

    card_3_frame.pack()

    card_4_frame = Frame(root)

    card_4_name_label = Label(card_4_frame, text=deck_array[3])
    card_4_name_label.config(font=(FONT, 11))
    card_4_name_label.pack()

    use4_button = Button(card_4_frame, text="Use Card", command=lambda: use_card(4, card_4_name_label))
    use4_button.config(font=(FONT, 11))
    use4_button.pack()

    card_4_frame.pack()


deck_creation_frame.pack()

mainloop()