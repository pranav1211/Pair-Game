import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Grid")

# Create frames for each row
for i in range(3):
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, padx=5, pady=5)

    # Create and pack buttons in each row
    for j in range(4):
        button = tk.Button(frame, text=f"Button {i*4 + j + 1}", command=button_click)
        button.pack(side=tk.LEFT)

# Start the Tkinter event loop
root.mainloop()
