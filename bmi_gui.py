import tkinter as tk

window= tk.Tk()

window.title("Martin's BMI Calculator")

# Label0
title = tk.Label(text="Welcome to Martin's BMI Calculator", bg = "magenta", fg= "cyan", font= "Times 32 bold italic ", bd=5, relief = "solid", width = 40) #format your text
title.grid( row = 0, columnspan = 2) #columnspan occupys more than 1 column


#function to display BMI
def display_BMI():
	height = float(entry1.get())
	weight = float(entry2.get())
	BMI = weight/height**2
	answer["text"] = "%.2f" % BMI
	
def display_clear():
	entry1.delete(0,100)
	entry2.delete(0,100)
	answer["text"] = ""
	entry1.focus() 
	
# Label1 for height
label1 = tk.Label(text="Enter height <m>: ", font = "Times 28", fg = "blue")
label1.grid(column = 0, row = 1,)

# Label2 for weight
label2 = tk.Label(text="Enter weight <kg>: ", font = "Times 28", fg = "blue")
label2.grid(column = 0, row = 2)

# Button to cal BMI
button1 = tk.Button(text = "Press to calculate BMI", font = "Times 28 bold italic",bg= "yellow",fg = "red", borderwidth = 20, relief = "raised", command=display_BMI)
button1.grid(column = 0, row = 3)

# Entry1 for height
entry1 = tk.Entry( font = "Times 28")
entry1.grid(column = 1, row = 1)

# Entry2 for weight
entry2 = tk.Entry( font = "Times 28") 
entry2.grid(column = 1, row = 2)

# Label3 display BMI
answer = tk.Label( text="", font = "Times 28 bold italic", fg = "green")
answer.grid(column = 1, row = 3)

# Button to clear
button1 = tk.Button(text = "Clear All", font = "Times 28 bold italic",bg= "yellow",fg = "red", borderwidth = 20, relief = "raised", command=display_clear)
button1.grid(row = 4, columnspan = 2)

#Make the entry box the focus by blinking
entry1.focus() 

# window keep checking for changes, if an event is triggered, especially if a button is pressed
window.mainloop() 

