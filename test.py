import tkinter as tk

def button_clicked(button_number):
    print(f"Button {button_number} clicked!")

# Create the main window
root = tk.Tk()
root.title("Centered Buttons")

# Create three buttons
button1 = tk.Button(root, text="Button 1", command=lambda: button_clicked(1))
button2 = tk.Button(root, text="Button 2", command=lambda: button_clicked(2))
button3 = tk.Button(root, text="Button 3", command=lambda: button_clicked(3))

# Pack the buttons with some space between them
button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=10)
button3.pack(side=tk.LEFT, padx=10)

# Start the main loop
root.mainloop()
