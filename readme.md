# ScreenCaptureTool

**ScreenCaptureTool** is a Python application designed for capturing a region of your screen, extracting text from the captured image using OCR, and copying the recognized text to your clipboard. It uses [pytesseract](https://github.com/madmaze/pytesseract) to perform Optical Character Recognition, [mss](https://github.com/BoboTiG/python-mss) for capturing screen snippets, and [pyperclip](https://github.com/asweigart/pyperclip) for copying recognized text directly to the system clipboard.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Building an Executable with PyInstaller](#building-an-executable-with-pyinstaller)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

1. **Screen Region Capture**  
   Press <kbd>Ctrl+Shift+Alt</kbd> to enter selection mode and drag a rectangle on any part of your screen.  

2. **OCR Text Extraction**  
   Once you release the mouse, the application automatically runs OCR on the selected screenshot to extract text.

3. **Clipboard Copy**  
   The recognized text is copied to the clipboard so you can easily paste it anywhere.

4. **Multi-Monitor Support**  
   Automatically detects your entire virtual screen area, allowing you to capture text from any monitor setup.

---

## Prerequisites

1. **Python 3.6+**  
   Ensure you have Python 3.6 or newer installed.

2. **Tesseract OCR**  
   - Install Tesseract if you haven't already. On Windows, you can download and install from:
     [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - On macOS (with Homebrew):  
     ```bash
     brew install tesseract
     ```
   - On most Linux distributions (for example, Ubuntu/Debian-based):
     ```bash
     sudo apt-get install tesseract-ocr
     ```

3. **Required Python Packages**  
   - `mss`
   - `pyperclip`
   - `pytesseract`
   - `screeninfo`
   - `keyboard`
   - `pillow`
   - `colorama`

You can install these packages using:
```bash
pip install mss pyperclip pytesseract screeninfo keyboard pillow colorama
```

---

## Installation

1. **Clone or Download the Repository**  
   ```bash
   git clone https://github.com/your-repo/ScreenCaptureTool.git
   cd ScreenCaptureTool
   ```

2. **Install the Required Packages**  
   ```bash
   pip install -r requirements.txt
   ```
   or individually:
   ```bash
   pip install mss pyperclip pytesseract screeninfo keyboard pillow colorama
   ```

3. **Set Tesseract Path (if necessary)**  
   If `tesseract` is not in your PATH, open the Python file (e.g., `app.py`) and uncomment (and update) the following line, providing the correct install path:
   ```python
   # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

---

## Usage

1. **Run the Application**  
   From the root directory, run:
   ```bash
   python app.py
   ```
   You should see:
   ```
   Press ctrl+shift+alt to capture any screen region (Esc+Shift to exit)
   ```

2. **Capture a Screenshot with OCR**  
   Press <kbd>Ctrl+Shift+Alt</kbd>:
   - The entire screen becomes lightly shaded.
   - Click and drag to select a rectangular region of the screen.
   - Once you release the mouse, the application extracts text from the selected area.

3. **Check the Recognized Text**  
   - If text is recognized successfully, it’s automatically copied to your clipboard.  
   - The application prints the recognized text in the console.

4. **Exit the Application**  
   Press <kbd>Esc+Shift</kbd> in the console to stop the application.

---

## Configuration

- **Hotkey**  
  The default hotkey is set in the code as:
  ```python
  KEY_COMBINATION = 'ctrl+shift+alt'
  ```
  You may change this to any valid hotkey combination recognized by the `keyboard` library.

- **Tesseract Executable Path**  
  If Tesseract is not detected in your system’s PATH, set the path manually in the script:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```
  Make sure to remove the preceding comment symbol (`#`).

---

## Building an Executable with PyInstaller

If you want to distribute this tool without requiring users to install Python or dependencies:

1. **Install PyInstaller**  
   ```bash
   pip install pyinstaller
   ```
2. **Build the Executable**  
   From your project directory, run:
   ```bash
   pyinstaller --onefile --console --icon=screenshot.ico --hidden-import=pytesseract -n ScreenCaptureTool app.py
   ```
   Explanation of flags:
   - `--onefile`: Produces a single executable file.
   - `--console`: Keeps console open (useful to see recognized text).
   - `--icon=screenshot.ico`: Sets a custom icon.
   - `--hidden-import=pytesseract`: Ensures PyInstaller includes `pytesseract`.
   - `-n ScreenCaptureTool`: Sets the name of the executable to *ScreenCaptureTool*.
   - `app.py`: The main Python file.

3. **Locate the Executable**  
   After a successful build, the executable will be inside the `dist` folder.

---

## Troubleshooting

1. **No text detected**  
   - Ensure the captured region has clear text.  
   - Zoom in if the text is small or low resolution.  
   - Check that Tesseract is installed and recognized (or manually set its path).

2. **Capture failed**  
   - On certain operating systems, you may need additional permissions for screen capturing.  
   - Verify that the region you’re selecting is visible (not behind another window).

3. **Hotkey conflicts**  
   - If <kbd>Ctrl+Shift+Alt</kbd> is already taken by another application, update the hotkey in the script.

4. **PyInstaller issues**  
   - If the PyInstaller executable fails to run or is missing modules, try adding them with `--hidden-import` or ensure your environment is properly set up.

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). 

Feel free to modify and distribute this application as needed. Contributions are welcome!

---

Thank you for using **ScreenCaptureTool**. If you have any issues or suggestions, please feel free to open an issue or create a pull request!

![image](https://github.com/user-attachments/assets/b1607bf0-f9bb-4601-881e-e95041ad795b)
