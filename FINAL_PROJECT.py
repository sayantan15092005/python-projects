import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", ".png;.jpg;.jpeg;.bmp;*.gif")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)
        global original_image
        original_image = Image.open(file_path)

def save_image(image, format):
    file_path = filedialog.asksaveasfilename(defaultextension=f".{format}",
                                             filetypes=[(f"{format.upper()} files", f"*.{format}")])
    if file_path:
        image.save(file_path, format=format.upper())
        messagebox.showinfo("Success", "Image converted and saved successfully!")

def convert_image():
    try:
        format = combo_format.get()
        width = entry_width.get()
        height = entry_height.get()

        if not format:
            raise ValueError("Please select a format.")

        if width and height:
            new_width = int(width)
            new_height = int(height)
            resized_image = original_image.resize((new_width, new_height))
        else:
            resized_image = original_image

        if format.lower() == 'jpeg':
            converted_image = resized_image.convert("RGB")
        else:
            converted_image = resized_image

        save_image(converted_image, format.lower())

    except ValueError as ve:
        messagebox.showwarning("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Image Converter")
root.geometry("450x400")

label_image_path = tk.Label(root, text="Select Image:")
label_image_path.pack(pady=10)

entry_image_path = tk.Entry(root, width=40)
entry_image_path.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=open_image)
button_browse.pack(pady=5)

label_preview = tk.Label(root)
label_preview.pack(pady=10)

label_format = tk.Label(root, text="Select Format:")
label_format.pack(pady=10)

combo_format = tk.StringVar()
combo_format.set("png")
dropdown_formats = tk.OptionMenu(root, combo_format, "png", "jpg", "jpeg", "bmp", "gif")
dropdown_formats.pack(pady=5)

label_resize = tk.Label(root, text="Resize Image (Width x Height):")
label_resize.pack(pady=10)

frame_resize = tk.Frame(root)
frame_resize.pack()

label_width = tk.Label(frame_resize, text="Width:")
label_width.pack(side=tk.LEFT)

entry_width = tk.Entry(frame_resize, width=5)
entry_width.pack(side=tk.LEFT, padx=5)

label_height = tk.Label(frame_resize, text="Height:")
label_height.pack(side=tk.LEFT)

entry_height = tk.Entry(frame_resize, width=5)
entry_height.pack(side=tk.LEFT, padx=5)

button_convert = tk.Button(root, text="Convert", command=convert_image)
button_convert.pack(pady=20)

root.mainloop()