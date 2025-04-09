import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while opening the file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def new_file():
    if text_area.get(1.0, tk.END).strip():
        response = messagebox.askyesno("Save Changes", "Do you want to save your changes?")
        if response:
            save_file()
    text_area.delete(1.0, tk.END)

def exit_app():
    if text_area.get(1.0, tk.END).strip():
        response = messagebox.askyesno("Save Changes", "Do you want to save your changes?")
        if response:
            save_file()
    root.quit()

def update_status(event=None):
    try:
        row, col = text_area.index(tk.INSERT).split(".")
        row, col = int(row), int(col)
        status_label.config(text=f"Line: {row} | Column: {col}")
    except Exception as e:
        print("Error updating status:", e)

# Initialize the main application window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Create the text area
text_area = tk.Text(root, wrap=tk.WORD, undo=True)
text_area.pack(expand=True, fill=tk.BOTH)
text_area.bind("<KeyRelease>", update_status)
text_area.bind("<ButtonRelease-1>", update_status)

# Create the menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Create the status bar
status_bar = tk.Frame(root)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
status_label = tk.Label(status_bar, text="Line: 1 | Column: 1", anchor="w", width=40, relief=tk.SUNKEN)
status_label.pack(fill=tk.X)

# Start the main application loop
root.mainloop()