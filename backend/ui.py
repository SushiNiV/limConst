import os
import tkinter as tk
from tkinter import font as tkFont
from PIL import ImageFont
from backend.logic import limConst

def compute():
    user_input = entry.get()
    result = limConst(user_input)
    result_label.config(text=f"Limit: {result}")

root = tk.Tk()
root.geometry("300x200")
root.resizable(True, True)
root.overrideredirect(True)

fontPath = os.path.join(os.getcwd(), "assets", "DePixelHalbfett.ttf")
if not os.path.exists(fontPath):
    print("❌ Error: Font file not found in assets folder.")
else:
    try:
        # Load the font using PIL
        font = ImageFont.truetype(fontPath, 12)
        fontName = font.getname()[0]  # Get the font name

        # Create a Tkinter font object (without tk.call)
        cFont = tkFont.Font(family=fontName, size=12)
    except Exception as e:
        print(f"❌ Error loading font: {e}")
        fontName = "Arial"  # Fallback font
        cFont = tkFont.Font(family=fontName, size=12)

# Title bar frame
titleBar = tk.Frame(root, bg="#1b1262", relief="raised", bd=2)
titleBar.pack(fill="x", side="top")

titleLabel = tk.Label(titleBar, text="Limit of a Constant Calculator", bg="#1b1262", fg="white", font=cFont)
titleLabel.pack(side="left", padx=10)

close_button = tk.Button(titleBar, text="✖", bg="red", fg="white", command=root.destroy, bd=0)
close_button.pack(side="right", padx=5)

def start_move(event):
    root.x = event.x_root
    root.y = event.y_root

def moving(event):
    new_x = root.winfo_x() + (event.x_root - root.x)
    new_y = root.winfo_y() + (event.y_root - root.y)
    root.geometry(f"+{new_x}+{new_y}")
    root.x, root.y = event.x_root, event.y_root

# Bind dragging events
titleBar.bind("<Button-1>", start_move)
titleBar.bind("<B1-Motion>", moving)

# Main UI frame
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 14))
entry.pack(pady=5, fill="x")

compute_button = tk.Button(frame, text="Calculate", font=("Arial", 12), command=compute)
compute_button.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Arial", 14))
result_label.pack(pady=5)

root.mainloop()
