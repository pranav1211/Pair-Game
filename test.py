from tkinter import Tk, Label

root = Tk()

for i in range(1, 13):
    label_text = str(i).replace('1', '2')
    label = Label(root,
                  text=label_text,
                  font=("Arial", 25),
                  bg="black",
                  fg='white',)
    label.pack()

root.mainloop()
