import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


# GUI
mainApp = tk.Tk()
mainApp.title("TD07 Image Converter")


def convert_jpg_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

    if file_path:
        img = Image.open(file_path)
        png_path = file_path.replace(".jpg", ".png")
        img.save(png_path, "PNG")
        
        # Extracting file name and directory
        selected_file_name = os.path.basename(file_path)
        png_file_name = os.path.basename(png_path)
        file_directory = os.path.dirname(file_path)

        # Pop-up Message
        status_message = f"Saved Image Details\n\n- JPG File:  {selected_file_name}\n- Converted File:  {png_file_name}\n- Saved File Directory: \n{file_directory}"
        messagebox.showinfo("Successfully Saved", status_message)



def convert_jfif_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jfif")])

    if file_path:
        img = Image.open(file_path)
        png_path = file_path.replace(".jfif", ".png")
        img.save(png_path, "PNG")
        
        # Extracting file name and directory
        selected_file_name = os.path.basename(file_path)
        png_file_name = os.path.basename(png_path)
        file_directory = os.path.dirname(file_path)

        # Pop-up Message
        status_message = f"Saved Image Details\n\n- JPG File:  {selected_file_name}\n- Converted File:  {png_file_name}\n- Saved File Directory: \n{file_directory}"
        messagebox.showinfo("Successfully Saved", status_message)



def convert_png_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])

    if file_path:
        img = Image.open(file_path)
        jpg_path = file_path.replace(".png", ".jpg")
        img.save(jpg_path, "JPEG")

        # Extracting file name and directory
        selected_file_name = os.path.basename(file_path)
        jpg_file_name = os.path.basename(jpg_path)
        file_directory = os.path.dirname(file_path)

        # Pop-up Message
        status_message = f"Saved Image Details\n\n- PNG File:  {selected_file_name}\n- Converted File:  {jpg_file_name}\n- Saved File Directory: \n{file_directory}"
        messagebox.showinfo("Successfully Saved", status_message)




# Content Directory
Content_directory = os.path.join(os.path.dirname(__file__), "ContentFiles")

# Icon Part
icon_path = os.path.join(Content_directory, "TD07ImageConverterIcon.ico")
mainApp.iconbitmap(default=icon_path)

# BG Image
BG_path = os.path.join(Content_directory, "ImageConverterBG.png")
BG_image = tk.PhotoImage(file=BG_path)

BG_Label = tk.Label(mainApp, image=BG_image, bg="#5271FF")
BG_Label.place(relwidth=1, relheight=1)

# Window width and height
mainApp.geometry("800x600")


# Background color
mainApp.configure(bg="#5271FF")

# Buttons
buttonFont = ("Lato", 12, "bold")

# First line of buttons
first_line_frame = tk.Frame(mainApp, bg="#5271FF")
first_line_frame.pack(side=tk.TOP, pady=(250, 0),  padx=(200, 0))

# Second line of buttons
second_line_frame = tk.Frame(mainApp, bg="#5271FF")
second_line_frame.pack()


# Convert JPG-2-PNG
convert_to_PNGbutton = tk.Button(first_line_frame, text="Convert JPG to PNG", font=buttonFont, command=convert_jpg_to_png, bg="#F0DBC1")
convert_to_PNGbutton.pack(pady=5, padx=(8, 30), side=tk.RIGHT)

# Convert PNG-2-JPG
convert_to_JPGbutton = tk.Button(first_line_frame, text="Convert PNG to JPG", font=buttonFont, command=convert_png_to_jpg, bg="#F0DBC1")
convert_to_JPGbutton.pack(pady=5, padx=0, side=tk.RIGHT)

# Convert JFIF-2-PNG
convert_to_JFIF2PNGbutton = tk.Button(second_line_frame, text="Convert JFIF to PNG", font=buttonFont, command=convert_jfif_to_png, bg="#F0DBC1")
convert_to_JFIF2PNGbutton.pack(pady=5, padx=(8, 15), side=tk.RIGHT)




mainApp.mainloop()
