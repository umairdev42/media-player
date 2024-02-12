import tkinter as tk
from tkinter import ttk
import subprocess

class PlayerExApp:
    def __init__(self, master):
        self.master = master
        master.title("Player Ex | Media Player")
        master.geometry("1280x720")  # Set an initial window size
        # Load the app icon
        logo_image = tk.PhotoImage(file="images/logo.png")  # Replace with the actual path to your image
        # Set the window icon
        master.iconphoto(True, logo_image)

        self.create_widgets()

    def create_widgets(self):
        # Create a Frame for the root window
        root_frame = ttk.Frame(self.master, padding="10", style="White.TFrame")
        root_frame.pack(fill=tk.BOTH, expand=True)

        # Create a Frame for the left side
        left_frame = ttk.Frame(root_frame, style="White.TFrame")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(75, 75))

        # Create a Label for the "PlayerEx" heading
        heading_label = ttk.Label(left_frame, text="Media", font=("Arial", 20, "bold"), style="Black.TLabel")
        heading_label.pack(pady=(50, 20))

        # Create buttons for the left side
        left_buttons = ttk.Frame(left_frame, style="White.TFrame")
        left_buttons.pack()

        for text, command in [("Audio Player", "audio-player.py"),
                              ("Video Player", "dependencies/GridPlayer.exe")]:
            button = ttk.Button(left_buttons, text=text, style="Grey.TButton",
                                command=lambda c=command: self.on_button_press(c))
            button.pack(ipadx=90, pady=(0, 10))

        # Create a label for the Features heading
        heading_label = ttk.Label(left_frame, text="Features", font=("Arial", 20, "bold"), style="Black.TLabel")
        heading_label.pack(pady=(50, 20))

        # Create buttons for the left side
        left_buttons = ttk.Frame(left_frame, style="White.TFrame")
        left_buttons.pack()

        for text, command in [("Audio Clipper", "audio-clipper.py"),
                              ("MP3 Converter", "video-converter.py"),
                              ("Extract Vocals", "dependencies/SpleeterGui.exe"),  # Provide the correct path
                              ("Enhance Video", "enhance-video.py")]:
            button = ttk.Button(left_buttons, text=text, style="Grey.TButton",
                                command=lambda c=command: self.on_button_press(c))
            button.pack(ipadx=90, pady=(0, 10))

        # Create a Frame for the right side
        right_frame = ttk.Frame(root_frame, style="Black.TFrame")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create an Image for the logo
        logo_img = tk.PhotoImage(file="images/logo.png")
        # Resize the logo image
        logo_img = logo_img.subsample(2)  # Reduce the size by a factor of 2
        logo_label = ttk.Label(right_frame, image=logo_img)
        logo_label.image = logo_img
        logo_label.pack(side=tk.RIGHT, padx=300, expand=False)

        # Make the window responsive
        self.master.columnconfigure(0, weight=1)
        root_frame.columnconfigure(0, weight=1)
        left_frame.columnconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def on_button_press(self, command):
        print(f"Button pressed for command: {command}")

        if command.endswith(".exe"):
            # Run the .exe file using subprocess.Popen
            subprocess.Popen([command])
        else:
            # For other commands, assume it's a Python script and run it with Python
            subprocess.Popen(["python", command])

def main():
    root = tk.Tk()
    app = PlayerExApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
