import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Grid")

# Create 3 frames for each row
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, padx=5, pady=5)

frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP, padx=5, pady=5)

frame3 = tk.Frame(root)
frame3.pack(side=tk.TOP, padx=5, pady=5)

# Place buttons in each frame
button1 = tk.Button(frame1, text="Button 1", command=button_click)
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame1, text="Button 2", command=button_click)
button2.pack(side=tk.LEFT)

button3 = tk.Button(frame1, text="Button 3", command=button_click)
button3.pack(side=tk.LEFT)

button4 = tk.Button(frame1, text="Button 4", command=button_click)
button4.pack(side=tk.LEFT)

button5 = tk.Button(frame2, text="Button 5", command=button_click)
button5.pack(side=tk.LEFT)

button6 = tk.Button(frame2, text="Button 6", command=button_click)
button6.pack(side=tk.LEFT)

button7 = tk.Button(frame2, text="Button 7", command=button_click)
button7.pack(side=tk.LEFT)

button8 = tk.Button(frame2, text="Button 8", command=button_click)
button8.pack(side=tk.LEFT)

button9 = tk.Button(frame3, text="Button 9", command=button_click)
button9.pack(side=tk.LEFT)

button10 = tk.Button(frame3, text="Button 10", command=button_click)
button10.pack(side=tk.LEFT)

button11 = tk.Button(frame3, text="Button 11", command=button_click)
button11.pack(side=tk.LEFT)

button12 = tk.Button(frame3, text="Button 12", command=button_click)
button12.pack(side=tk.LEFT)

# Start the Tkinter event loop
root.mainloop()
