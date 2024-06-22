import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# count for global total cards
flashcards = {"Powerhouse of the cell":"Mitochondria","Brain of the cell":"Nucleus",
            "Protective layer of the cell":"Cell Membrane",
            "Food Storage of the cell":"Vacuole","Jelly of the cell":"Cytoplasm", 
            "Killer of the cell":"Lysosome"}
global keys
global current_cardindex
keys = list(flashcards.keys())
current_cardindex = 0
totalcards = 6

# load words in csv file into flashcard dictionary

###############

# TODO: randomize card order

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
    keys = list(flashcards.keys())
    current_cardindex = 0
    
    if totalcards > 0:
        show_question()

current_cardindex = 0

def show_question():
    global current_cardindex
    question_label.config(text=keys[current_cardindex])
    answer_label.config(text="")

def show_answer():
    global current_cardindex
    answer_label.config(text=flashcards[keys[current_cardindex]])

def right_pressed():
    global current_cardindex
    if current_cardindex < totalcards - 1:
        current_cardindex += 1
    else:
        current_cardindex = 0
    show_question()

def left_pressed():
    global current_cardindex
    if current_cardindex > 0:
        current_cardindex -= 1
    else:
        current_cardindex = totalcards - 1
    show_question()

###############

root = tk.Tk()
root.title('Flashcards Player')

# set fixed size
width = 600
height = 400
root.geometry(f"{width}x{height}")
root.resizable(False, False)
root.minsize(600,400)

# header
header = tk.Label(root, text='Let\'s play flashcards!', font='Helvetica 18 bold')
header.pack()

subtitle = tk.Label(root, text='To play, please upload a CSV file with two columns for question and answers, with no header row. \nA sample file is provided in the folder.', font='Helvetica 10')
subtitle.pack()

# note: supposed to load csv file, for now it will exit program
button = tk.Button(root, text='Load CSV File', width=25, command=upload_file)
button.pack()

# create question frame
questiontext_frame = tk.Frame(root)
questiontext_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
questiontext_label = tk.Label(questiontext_frame, text="QUESTION", font=('Calibri', 10))
questiontext_label.pack(side=tk.TOP)

question_frame = tk.LabelFrame(root, width= 500, height= 50, bd=5)
question_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
question_frame.propagate(False)
question_label = tk.Label(question_frame, text=keys[0], font=('Calibri', 15))
question_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

answertext_frame = tk.Frame(root)
answertext_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
answertext_label = tk.Label(answertext_frame, text="ANSWER", font=('Calibri', 10))
answertext_label.pack(side=tk.TOP)

answer_frame = tk.LabelFrame(root, width= 500, height= 50, bd=5)
answer_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
answer_frame.propagate(False)
answer_label = tk.Label(answer_frame, text="", font=('Calibri', 15))
answer_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# buttons to switch cards
left_button = tk.Button(root, text="<--", command=left_pressed)
left_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

right_button = tk.Button(root, text="-->", command=right_pressed)
right_button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

show_button = tk.Button(root, text="Show Answer", command=show_answer)
show_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()