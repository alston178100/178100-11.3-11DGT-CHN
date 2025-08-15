from tkinter import *

root = Tk(className="tkinter practice 1")

# Settnig the window size to 400 x 400 pixels
root.geometry("400x400")

# Create a label widget (Text) with the text "Hello World!"
# The .pack() method packs the label into the window
test_msg = Label(root, text="Hello World!")
test_msg.pack()

# Buttons can be clicked and perform actions based on the command
# Padding inside the pack() method is equivalent to margin in CSS
button = Button(root, text="Button!!", width=40, command=root.destroy)
button.pack(pady=20)

# Entry widget allows user input in form of text
# The grid() geometry manager organizes widgets in a table-like structure
entry1 = Entry(root)
entry2 = Entry(root)
entry1.pack(pady=5)
entry2.pack(pady=5)

# Contiuously runs loop
root.mainloop()
