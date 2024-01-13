import tkinter as tk

def update_score():
    # Increment the score by 1 on each button press
    score_var.set(score_var.get() + 1)
    # Update the label text with the new score
    score_label.config(text=f"Score: {score_var.get()}")

# Create the main window
root = tk.Tk()
root.title("Score Example")

# Initialize the score variable
score_var = tk.IntVar()
score_var.set(0)

# Create a Label to display the current score
score_label = tk.Label(root, text=f"Score: {score_var.get()}")
score_label.pack(pady=10)

# Create a Button to trigger the update of the score
update_button = tk.Button(root, text="Increase Score", command=update_score)
update_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
