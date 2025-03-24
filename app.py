import tkinter as tk
import keyboard
import pyperclip
from PIL import Image
import mss
import mss.tools
from screeninfo import get_monitors
from io import BytesIO
from colorama import Fore, Style
import pytesseract

# Use the following line to set the path to the Tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

KEY_COMBINATION = 'ctrl+shift+alt'

class ScreenshotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

        # Get virtual screen dimensions
        monitors = get_monitors()
        self.virtual_left = min(m.x for m in monitors)
        self.virtual_top = min(m.y for m in monitors)
        self.virtual_right = max(m.x + m.width for m in monitors)
        self.virtual_bottom = max(m.y + m.height for m in monitors)
        
        self.screen_width = self.virtual_right - self.virtual_left
        self.screen_height = self.virtual_bottom - self.virtual_top

        # Set window to cover all screens
        self.root.geometry(f"{self.screen_width}x{self.screen_height}" f"+{self.virtual_left}+{self.virtual_top}")

        self.canvas = tk.Canvas(self.root, bg='white', highlightthickness=0, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.root.mainloop()

    def to_canvas_coords(self, x, y):
        """Convert screen coordinates to canvas coordinates"""
        return x - self.virtual_left, y - self.virtual_top

    def to_screen_coords(self, x, y):
        """Convert canvas coordinates to screen coordinates"""
        return x + self.virtual_left, y + self.virtual_top

    def on_press(self, event):
        # Get absolute screen coordinates
        screen_x = self.root.winfo_pointerx()
        screen_y = self.root.winfo_pointery()
        
        # Convert to canvas coordinates
        self.start_x, self.start_y = self.to_canvas_coords(screen_x, screen_y)
        
        # Create rectangle in canvas coordinates
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y,
            self.start_x, self.start_y,
            outline='black', fill='black', width=4
        )

    def on_drag(self, event):
        # Get current screen coordinates
        screen_x = self.root.winfo_pointerx()
        screen_y = self.root.winfo_pointery()
        
        # Convert to canvas coordinates
        cur_x, cur_y = self.to_canvas_coords(screen_x, screen_y)
        
        # Update rectangle in canvas coordinates
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        # Get final screen coordinates
        end_screen_x = self.root.winfo_pointerx()
        end_screen_y = self.root.winfo_pointery()
        self.root.destroy()

        # Convert to screen coordinates
        start_screen_x, start_screen_y = self.to_screen_coords(self.start_x, self.start_y)
        
        # Calculate capture area
        left = min(start_screen_x, end_screen_x)
        top = min(start_screen_y, end_screen_y)
        right = max(start_screen_x, end_screen_x)
        bottom = max(start_screen_y, end_screen_y)
        width = right - left
        height = bottom - top

        if width > 1 and height > 1:
            with mss.mss() as sct:
                monitor = {
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                    "mon": -1  # Capture from all monitors
                }
                try:
                    sct_img = sct.grab(monitor)
                    image_bytes = mss.tools.to_png(sct_img.rgb, sct_img.size, output=None)

                    # OCR processing
                    img = Image.open(BytesIO(image_bytes))
                    text = pytesseract.image_to_string(img).strip()

                    if text:
                        pyperclip.copy(text)
                        print(f"📋 Text copied to clipboard\n")
                        print("📄 Extracted text:\n" + "-" * 40)
                        print(text)
                        print("-" * 40)
                    else:
                        print("🔍 No text detected in selection")

                except Exception as e:
                    print(f"X Capture failed: {str(e)} X")
                    print("!!! Make sure the selection is visible on screen !!!")


def start_screenshot_app():
    ScreenshotApp()

# Required installations:
# pip install mss pyperclip pytesseract screeninfo keyboard pillow colorama

keyboard.add_hotkey(KEY_COMBINATION, start_screenshot_app)
print(f"Press {KEY_COMBINATION} to capture any screen region (Esc to exit)")
keyboard.wait('esc')


# pyinstaller --onefile --console --icon=screenshot.ico --hidden-import=pytesseract -n ScreenCaptureTool app.py