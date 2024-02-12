import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip
import threading
import shutil
import sys
sys.setrecursionlimit(3000)

def open_file():
    button.config(state=tk.DISABLED)
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    threading.Thread(target=convert_to_mp3, args=(file_path,)).start()

def convert_to_mp3(file_path):
    try:
        if file_path:
            video = VideoFileClip(file_path)
            mp3_file_path = os.path.splitext(file_path)[0] + ".mp3"
            video.audio.write_audiofile(mp3_file_path)
            print("File converted to MP3:", mp3_file_path)
            status_label.config(text="Conversion successful")
            save_button = tk.Button(root, text="Save File", command=lambda: save_file(mp3_file_path), bg="red", fg="white", padx=3, pady=3, width=12)
            save_button.pack(pady=10)
    except Exception as e:
        print("Error:", str(e))
        status_label.config(text="Error during conversion")
    finally:
        button.config(state=tk.NORMAL)


def save_file(mp3_file_path):
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    if save_path:
        shutil.move(mp3_file_path, save_path)
        status_label.config(text="File is Saved")


root = tk.Tk()
root.title("Video Converter")
root.geometry("1280x720")
# Load the image
logo_image = tk.PhotoImage(file="images/logo.png")  # Replace with the actual path to your image
# Set the window icon
root.iconphoto(True, logo_image)

# Create a Label widget for the heading
heading_label = tk.Label(root, text="Video Converter", font=("Arial", 28, "bold"))
heading_label.pack(pady=10)

#add image to the window
image_path = "images/logo.png"  # Replace with the actual path to your image
img = tk.PhotoImage(file=image_path)

# Create a Label widget to display the image with padding
image_label = tk.Label(root, image=img, width=400, height=400)
image_label.pack(padx=2, pady=2)

button = tk.Button(root, text="Select Video File", command=open_file, bg="red", fg="white", padx=3, pady=3)
button.pack(pady=20)

file_label = tk.Label(root, text="")
file_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
