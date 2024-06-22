import csv
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# count for global total cards
totalcards = 0

# load words in csv file into flashcard dictionary

'''
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
'''


###############
'''
print("Let's play flashcards!")

flashcards = load_flashcards('flashcards.csv')

play_flashcards(flashcards)
'''
###############

#this section is for all commands


# function for csv file upload
def upload_file():

    csv_filename = tk.filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if not csv_filename:
        return  # exit if no selected file

    global totalcards
    flashcards = dict() #list of cards

    # set default csv file if no input
    if csv_filename is None:
        csv_filename = 'flashcards.csv'

    # open csv file into the reader: csv_reader
    try:
        with open(csv_filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row:
                    flashcards[row[0]] = row[1]
                    totalcards += 1
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred: {e}")
    
    global keys
    keys = list(flashcards.keys())

    return flashcards

current_cardindex = 0

def right_pressed():
    if current_cardindex < totalcards:
        question_label.config(keys[current_cardindex])

def left_pressed():
    if current_cardindex > 0:
        current_cardindex -= 1
        question_label.config(keys[current_cardindex])

###############

root = tk.Tk()
root.title('Flashcards Player')

# set fixed size
width = 400
height = 300
root.geometry(f"{width}x{height}")
root.resizable(False, False)

# header
header = tk.Label(root, text='Let\'s play flashcards!')
header.pack()

# note: supposed to load csv file, for now it will exit program
button = tk.Button(root, text='Load CSV File', width=25, command=upload_file)
button.pack()

# create question frame
question_frame = tk.Frame(root, highlightbackground="black", highlightthickness=2)
question_frame.pack(side=tk.TOP)

# create answer frame -> but don't pack yet
answer_frame = tk.Frame(root,highlightbackground="black", highlightthickness=2) 
# TODO: answer frame should stay under question, 
# right there and show up only when press for answer

# create flashcard displayer
question_label = tk.Label(question_frame, text="PLACEHOLDER", font=('Calibri', 20))
question_label.pack(side=tk.TOP)
answer_label = tk.Label(answer_frame, text=" ", font=('Calibri', 20), fg='green')

# buttons to switch cards
left_button = tk.Button(root, text="<--")
left_button.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

right_button = tk.Button(root, text="-->")
right_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

show_button = tk.Button(root, text="Show Answer")
show_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

load_button = tk.Button(root, text="Load CSV")
load_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

root.mainloop()