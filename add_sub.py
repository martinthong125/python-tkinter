import tkinter as tk

window = tk.Tk()

window.title("Martin's Addition Calculator")

# Label0 ***Optional***
# format the text in the title
title = tk.Label(
    text="Welcome to Martin's Addition Calculator",
    bg="magenta",
    fg="cyan",
    font="Times 32 bold italic ",
    bd=5,
    relief="solid",
    width=40,
)
# columnspan occupys more than 1 column
title.grid(row=0, columnspan=2)

# function to add and display the sum
def display_sum():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    total = num1 + num2
    total1 = round(total, 2)
    result["text"] = total1


# function to subtract and display the subtraction
def display_sub():
    num2 = float(entry2.get())
    num3 = float(entry3.get())
    total = num2 - num3
    total1 = round(total, 2)
    result["text"] = total1


# Label1 for num1
label1 = tk.Label(text="Enter the first number, A: ", font="Times 28", fg="blue")
label1.grid(column=0, row=1)

# Label2 for num2
label2 = tk.Label(text="Enter the second number, B: ", font="Times 28", fg="blue")
label2.grid(column=0, row=2)

# Label3 for num3
label3 = tk.Label(text="Enter the third number, C: ", font="Times 28", fg="blue")
label3.grid(column=0, row=3)

# Button to cal sum
button1 = tk.Button(
    text="A+B",
    font="Times 28 bold italic",
    bg="yellow",
    fg="red",
    borderwidth=20,
    relief="raised",
    command=display_sum,
)
button1.grid(column=0, row=4)

# Button to cal subtraction
button1 = tk.Button(
    text="B-C",
    font="Times 28 bold italic",
    bg="yellow",
    fg="red",
    borderwidth=20,
    relief="raised",
    command=display_sub,
)
button1.grid(column=0, row=5)

# Entry1 for num1
entry1 = tk.Entry(font="Times 28")
entry1.grid(column=1, row=1)

# Entry2 for num2
entry2 = tk.Entry(font="Times 28")
entry2.grid(column=1, row=2)

# Entry3 for num3
entry3 = tk.Entry(font="Times 28")
entry3.grid(column=1, row=3)

# Label4 display sum
result = tk.Label(text="", font="Times 28 bold italic", fg="green")
result.grid(column=1, row=4)

# Make the entry box the focus by blinking
entry1.focus()

# window keep checking for changes to see if an event(eg. mouse click, key pressed) is triggered
window.mainloop()
