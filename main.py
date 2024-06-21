import csv
import random
import tkinter as tk

# count for global total cards
totalcards = 0

# class for flashcards (front and back side)
class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

# load words in csv file into flashcard format
def load_flashcards(csv_filename):
    global totalcards
    flashcards = [] #list of cards

    # open csv file into the reader: csv_reader
    with open(csv_filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row:
                flashcards.append(Card(row[0], row[1]))
                totalcards += 1

    return flashcards

# int for collecting points


# shuffle cards random
def play_flashcards(flashcards):
    points = 0
    random.shuffle(flashcards)

    for card in flashcards:
        validanswer = False
        while (validanswer == False): 
            x = input(f"{card.front}\nDo you know the answer? (Y/N)")

            # conditions for scoring
            if x == "Y":
                points += 1
                validanswer = True
            elif x == "N":
                validanswer = True
            else: #if answer is not Y or N
                print("invalid answer, please try again.")

        print(f"{card.back}\n")

    print(f"Finish! Your score is {points} out of {totalcards}.")

###############
'''
print("Let's play flashcards!")

flashcards = load_flashcards('flashcards.csv')

play_flashcards(flashcards)
'''
###############

root = tk.Tk()
root.title('Counting Seconds')
w = tk.Label(root, text='Let\'s play flashcards!')
button = tk.Button(root, text='Exit Program', width=25, command=root.destroy)

w.pack()
button.pack()
root.mainloop()