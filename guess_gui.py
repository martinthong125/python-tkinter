import random
rand_num = random.randint(1,99)
print(rand_num)
count = 0 #keep track the number of guesses
guess_list = [] #store all the guesses
low = 1
high = 99

import tkinter as tk

window= tk.Tk()
window.configure(background='black')

window.title("Martin's Number Guessing Game")

# Label0
title = tk.Label(text="Welcome to Martin's Number Guessing Game", bg = "magenta", fg= "cyan", font= "Times 32 bold italic ", bd=5, relief = "solid", width = 40) #format your text
title.grid( row = 0, columnspan = 2) #columnspan occupys more than 1 column

def gen_rand_num():
	global count, rand_num, guess_list, low, high
	rand_num = random.randint(1,99)
	print(rand_num)
	low = 1
	high = 99
	count = 0
	guess_list = []
	
def display_message():
	global count # to declare the variable "count" in the function and outside of the function as the same
	global print_guesses, guess_list, low, high
	count = count + 1
	label3["text"]= "Number of tries = " + str(count)
	num = int(entry.get())
	guess_list.append(num)
	entry.delete(0,100)
	if (num == rand_num):
		label2["text"] = "You guessed correctly! It is " + str(rand_num)
		button1.config(state="disabled") #disable button1
	elif (count == 8):
		label2["text"] = "You failed to guess the number. It is " + str(rand_num)
		button1.config(state="disabled") #disable button1
	elif (num > rand_num):
		label2["text"] = "Guess is too high."
		high = num
		label1["text"] = "Enter a number from " +str(low) + " to " + str(high)
		label4["text"] = "Wrong guesses = " + str(guess_list)[1:-1]
	else:
		label2["text"] = "Guess is too low."
		low = num
		label1["text"] = "Enter a number from " +str(low) + " to " + str(high)
		label4["text"] = "Wrong guesses = "+ str(guess_list)[1:-1]
		
def display_clear():
	gen_rand_num()
	count = 0
	button1.config(state="normal") #enable button1
	entry.delete(0,100)
	label1["text"] = "Enter a number from " +str(low) + " to " + str(high)
	label2["text"] = ""
	label3["text"] = "Number of tries = "
	label4["text"] = "Wrong guesses ="
		
# Label1 for enter number
label1 = tk.Label(text="Enter a number from " +str(low) + " to " + str(high), font = "Times 28", bg = "black", fg = "orange")
label1.grid(row = 1, columnspan = 2)

# Entry field for number
entry = tk.Entry( font = "Times 28")
entry.grid(row = 3, column = 0, sticky="e")

# Button to confirm number
button1 = tk.Button(text = "Enter", font = "Times 28 bold italic",bg= "yellow",fg = "red", borderwidth = 20, relief = "raised", command=display_message)
button1.grid(column = 1, row = 3)

# label2 for message field
label2 = tk.Label(text="", font = "Times 28", bg = "black", fg = "magenta")
label2.grid(row = 4, columnspan = 2)

# label3 for number of tries
label3 = tk.Label(text="Number of tries = " + str(count), font = "Times 20", bg = "black", fg = "light green")
label3.grid(column = 0, row = 5, sticky = "w")

# label4 for guesses
label4 = tk.Label(text="Wrong guesses =", font = "Times 20", bg = "black", fg = "light green")
label4.grid(column = 0, row = 6, sticky = "w")

# Button to restart game
button2 = tk.Button(text = "Restart game", font = "Times 28 bold italic",bg= "yellow",fg = "red", borderwidth = 20, relief = "raised", command=display_clear)
button2.grid(row = 7, columnspan = 2)

#Make the entry box the focus by blinking
entry.focus() 

# window keep checking for changes, if an event is triggered, especially if a button is pressed
window.mainloop() 
