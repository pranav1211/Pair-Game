from tkinter import *
root = Tk()

def message():
    L['text'] = 'I LIKE ICE CREAM'

def delay():
    L['text'] = 'Wait for it...'
    root.after(2000, message)

L = Label(root, text="Please click the button.")
L.pack()

B = Button(root, text="button", command=delay)
B.pack()

root.mainloop()