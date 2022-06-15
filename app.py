import tkinter as tk


# funtion, for loop, if statement
def show_output():
    number = int(number_input.get())
    if number == 0:
        output_label.configure(text="""Note:
            The Result for your request is not going to print
            because any digit multiply to zero it returns value zero""")
        return

    output = ""
    for i in range(1, 11):
        output += str(number) + " x " + str(i)
        output += " = " + str(number * i) + "\n"
    output_label.configure(text=output)


    # frame
window = tk.Tk()
window.title("Multiplication Table in Python")
window.minsize(width=450, height=450)

# title
title_label = tk.Label(master=window, text="Table")
title_label.pack(pady=20)

# user assign number
number_input = tk.Entry(master=window, width=30)
number_input.pack()

# button
submit_button = tk.Button(master=window, text="Submit",
                          command=show_output, width=15, height=2,)
submit_button.pack()

# output
output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
