import cv2
import tkinter as tk
from tkinter import filedialog
import subprocess

cv2.namedWindow('Webcam Feed', cv2.WINDOW_GUI_NORMAL)


# Function to open a text file
def open_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        subprocess.run(["notepad.exe", file_path])

# Create a GUI window
root = tk.Tk()
root.title("Face Detection and Text File Opener")

# Create a button to open a text file
open_button = tk.Button(root, text="Open Text File", command=open_text_file, state="disabled")
open_button.pack()

# Initialize the webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:/Users/AviNoronha/Desktop/GIT1/python/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        open_button["state"] = "normal"  # Enable the button when a face is detected
    else:
        open_button["state"] = "disabled"  # Disable the button when no face is detected

    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
root.mainloop()
