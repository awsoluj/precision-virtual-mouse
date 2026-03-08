Precision Virtual Mouse 🖱️

This project is a Python application that allows you to control your mouse using hand gestures captured through your computer's webcam. It leverages MediaPipe and OpenCV for hand tracking and PyAutoGUI to perform system-level mouse actions.

Note: This project has been developed and tested specifically on Python 3.10.11. Using other versions may lead to compatibility issues with certain libraries (especially MediaPipe).

Features

Precision Cursor Control: Manage the mouse pointer via the movement of your index finger.

Clicking: Perform a left-click by quickly pinching your thumb and index finger together and releasing.

Dragging: Hold your fingers pinched to drag files or windows across the screen.

Smooth Movement: Includes a smoothing algorithm to prevent jitter and shaky cursor movements.

Responsive Scaling: Automatically adapts to different screen resolutions.

Installation

Clone this repository:

git clone [https://github.com/yourusername/precision-virtual-mouse.git](https://github.com/yourusername/precision-virtual-mouse.git)
cd precision-virtual-mouse


Ensure you are using Python 3.10.11. You can check your version with:

python --version


Install the required libraries:

pip install -r requirements.txt


Usage

To start the project, run the main.py file or double-click the start.bat file if you are on Windows:

python main.py


Control Gestures

Move Mouse: Show your index finger to the camera and move it.

Left Click: Pinch your thumb and index finger together and release in less than 0.35 seconds.

Dragging: Pinch your fingers together and hold for more than 0.35 seconds. Releasing the pinch ends the drag.

Exit: Press the q key on your keyboard while the application window is focused.

Requirements

Python 3.10

Libraries listed in requirements.txt
