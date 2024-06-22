import csv
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# count for global total cards
flashcards = {}
global keys
global current_cardindex
keys = list(flashcards.keys())
current_cardindex = 0
totalcards = 0
file_uploaded = False

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
    csv_filename = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if not csv_filename:
        return  # Exit if no file is selected

    global totalcards
    global flashcards  # List of cards

    # Remove the old flashcards and reset totalcards
    flashcards = dict()
    totalcards = 0

    # Open CSV file and load into the flashcards dictionary
    try:
        with open(csv_filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row:
                    flashcards[row[0]] = row[1]
                    totalcards += 1
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    
    global keys
    global current_cardindex
    global file_uploaded
    keys = list(flashcards.keys())
    current_cardindex = 0
    file_uploaded = True
    
    if totalcards > 0:
        show_question()

current_cardindex = 0

def show_question():
    global current_cardindex
    question_label.config(text=keys[current_cardindex])
    answer_label.config(text="")

def show_answer():
    global current_cardindex
    if file_uploaded == True:
        answer_label.config(text=flashcards[keys[current_cardindex]])

def right_pressed():
    global current_cardindex
    if file_uploaded == True:
        if current_cardindex < totalcards - 1:
            current_cardindex += 1
        else:
            current_cardindex = 0
        show_question()

def left_pressed():
    global current_cardindex
    if file_uploaded == True:
        if current_cardindex > 0:
            current_cardindex -= 1
        else:
            current_cardindex = totalcards - 1
        show_question()

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
question_frame = tk.Frame(root)
question_frame.pack(side=tk.TOP)

# create answer frame -> but don't pack yet
answer_frame = tk.Frame(root,highlightbackground="black", highlightthickness=2) 
# TODO: answer frame should stay under question, 
# right there and show up only when press for answer

# create flashcard displayer
question_label = tk.Label(question_frame, text=" ", font=('Calibri', 20))
question_label.pack(side=tk.TOP)
answer_label = tk.Label(root, text="", font=('Calibri', 20), fg='white')
answer_label.pack()

# buttons to switch cards
left_button = tk.Button(root, text="<--", command=left_pressed)
left_button.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

right_button = tk.Button(root, text="-->", command=right_pressed)
right_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

show_button = tk.Button(root, text="Show Answer", command=show_answer)
show_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()