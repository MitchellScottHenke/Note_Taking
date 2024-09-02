"""
Building a note-taking app
With a GUI
Trying to follow Gemini
"""

# Import module (Tkinter)
import tkinter as tk
from tkinter.filedialog import askopenfilename

# Create the main window
root = tk.Tk()
root.title("Note-Taking App")

# Create widgets
text_box = tk.Text(root, height=5, width=50)
text_box.pack()

save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack()


# Handle Events
def save_note():
    # Code to save the note
    filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(text_box.get(1.0, tk.END))


root.mainloop()
