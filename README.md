# Precision Virtual Mouse 🖱️

A Python-based system utility controlled entirely by hand gestures using MediaPipe and OpenCV. It allows you to control your OS mouse cursor, click, and drag without touching your hardware.

## ⚠️ Important: Python Version
**Required Python Version:** Python 3.10.x  
This project is optimized for **Python 3.10**. Newer versions (like 3.12 or 3.13) will cause errors with MediaPipe.

👉 **[Download Python 3.10.11 Here (Direct Installer)](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)**

> **Installation Note:** When installing Python, make sure to check the box **"Add Python to PATH"** at the bottom of the installer window.

## 🖱️ Controls

* **Move Cursor:** Point your Index Finger and move it across the camera frame.

* **Left Click:** Quick Pinch (bring index finger and thumb together and release within 0.35s).

* **Drag & Drop:** Hold Pinch (bring index finger and thumb together and keep them closed to drag windows or files).

* **Quit:** Press **'q'**.

## 🚀 How to Run (Easy Way)

Clone or download this repository.

Double-click on **`start.bat`**.
(It will automatically install dependencies and launch the application.)

## 🛠️ How to Run (Manual Way)

If you prefer running it manually via terminal:

1. Create a virtual environment (Python 3.10):
    ```bash
    python -m venv venv
    ```

2. Activate the environment:
    ```bash
    Windows: venv\Scripts\activate
    Mac/Linux: source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```
