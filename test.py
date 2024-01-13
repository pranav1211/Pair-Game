import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Grid")

# Create and pack buttons in 3 rows and 4 columns
for i in range(3):
    for j in range(4):
        button = tk.Button(root, text=f"Button {i*4 + j + 1}", command=button_click)
        button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
