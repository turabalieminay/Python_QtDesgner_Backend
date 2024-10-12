# License Plate Recognition System

## Overview
This project is a **License Plate Recognition System** developed using Python and PyQt5. It utilizes a graphical user interface (GUI) to detect and recognize license plates from video feeds or images. The project is designed with **Qt Designer** and consists of two primary components:

1. **Video Input/Feed**: Displays the live video feed or image.
2. **License Plate Detection**: Detects and extracts license plate information from the video or image and displays it in a table.

## Features
- **Real-Time License Plate Detection**: Automatically detects license plates in a video feed or static images.
- **Graphical User Interface**: Built with PyQt5, offering a user-friendly interface to view video streams and detected license plates.
- **Data Logging**: Detected license plates are displayed in a table for easy tracking and review.

## Project Structure
- `main.py`: The main Python file that runs the license plate recognition system.
- `ui.py`: Contains the PyQt5 interface generated using **Qt Designer**.
- `resources/`: Directory containing any resources, such as images or additional files.
- `README.md`: This file, which provides an overview and usage instructions for the project.

## Installation
### Prerequisites
Make sure you have the following dependencies installed:

- Python 3.x
- PyQt5 (`pip install PyQt5`)
- OpenCV (`pip install opencv-python`)

### Steps to Run
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/license-plate-recognition.git
   cd license-plate-recognition
