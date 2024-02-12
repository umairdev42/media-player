import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import sys
sys.setrecursionlimit(3000)

def process_video():
    file_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video files", "*.mp4;*.avi")])

    if file_path:
        cap = cv2.VideoCapture(file_path)

        # Get video properties
        width = int(cap.get(3))
        height = int(cap.get(4))
        fps = int(cap.get(5))

        # Create VideoWriter object to save the processed video
        save_path = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("Video files", "*.avi")])
        if not save_path:
            return

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Sharpening using addWeighted()
            sharpened = cv2.addWeighted(frame, 7.5, cv2.GaussianBlur(frame, (7, 7), 2), -6.5, 0)

            # Apply bilateral blur
            bilateral_blur = cv2.bilateralFilter(sharpened, 9, 75, 75)

            # Display the original, sharpened, and blurred video frames
            # cv2.imshow("Enhanced Video", frame)
            # cv2.imshow("Original Video", sharpened)
            # cv2.imshow("Blurred Video", bilateral_blur)

            # Write the processed frame to the output video
            out.write(bilateral_blur)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # Enable Save button
        save_button.config(state=tk.NORMAL)

        # Store the processed video path in the global variable for saving
        global processed_video_path
        processed_video_path = save_path

def save_video():
    save_path = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("Video files", "*.avi")])
    if save_path and processed_video_path:
        # Copy the processed video file to the user-specified location
        import shutil
        shutil.copyfile(processed_video_path, save_path)
        print(f"Processed video saved to {save_path}")

# Create the main application window
app = tk.Tk()
app.title("Video Enhancer")
app.geometry("1280x720")

# Load the app icon
logo_image = tk.PhotoImage(file="images/logo.png")  # Replace with the actual path to your image
# Set the window icon
app.iconphoto(True, logo_image)

# Create a Label widget for the heading
heading_label = tk.Label(app, text="Video Enhancer", font=("Arial", 28, "bold"))
heading_label.pack(pady=10)

#add image to the window
image_path = "images/logo.png"  # Replace with the actual path to your image
img = tk.PhotoImage(file=image_path)

# Create a Label widget to display the image with padding
image_label = tk.Label(app, image=img, width=400, height=400)
image_label.pack(padx=2, pady=2)

# Create and pack a button to trigger video processing
process_button = tk.Button(app, text="Process Video", command=process_video, bg="red", fg="white")
process_button.pack(padx=20, pady=20)

# Create and pack a button to save the processed video (initially disabled)
save_button = tk.Button(app, text="Save Video", command=save_video, state=tk.DISABLED, bg="red", fg="white")
save_button.pack(padx=20, pady=20)

# Run the Tkinter main loop
app.mainloop()
