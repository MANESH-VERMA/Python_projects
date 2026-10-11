import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content) # Fixed: Inserted the read content variable


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Save File", "File saved successfully!")


root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

menu = tk.Menu(root) # Fixed: Changed tl.Menu to tk.Menu
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label="File", menu=file_menu) # Fixed: Changed add_command to add_cascade
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)

# Note: This block will raise a TclError in Google Colab.
# Please copy and run this script locally on your computer to test the GUI.
try:
    root.mainloop()
except Exception as e:
    print(f"Could not start GUI: {e}\nRun this script locally on your machine to display the UI!")