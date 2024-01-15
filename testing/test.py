import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Button with Image")

# Create a PhotoImage object from an image file (make sure the file path is correct)
image = tk.PhotoImage(file="path/to/your/image.png")

# Create a Button with the image
button = tk.Button(root, image=image, command=button_click)
button.pack(pady=10)

# Create a Label to display a message when the button is clicked
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
