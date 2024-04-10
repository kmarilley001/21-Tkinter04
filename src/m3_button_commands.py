

import tkinter as tk
entries = []
def print_form():
    for entry_box in entries:
        print(entry_box.get())



window = tk.Tk()
window.title("Fillable Form")


form_frame = tk.Frame(window, padx=10, pady=10)
form_frame.pack()

labels = [
    "Name: ",
    "Address Line 1: ",
    "Address Line 2: ",
    "City: ",
    "State: ",
    "Zip code: ",
    "Phone Number: ",
    "Email Address: "
]


for label_text in labels:
    label = tk.Label(form_frame, text=label_text, width=15, anchor="w")
    label.grid(sticky="w", pady=5)

    entry = tk.Entry(form_frame, width=30)
    entries.append(entry)
    entry.grid(row=labels.index(label_text), column=1, padx=(0, 10))

submit_button = tk.Button(window, text="Submit", width=10, height=2, fg="red", bg="white", command = print_form)
submit_button.pack(pady=10)

window.mainloop()















###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################