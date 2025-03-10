# PyQt6 Drawing App

## Description
This is a simple drawing application built with PyQt6. Users can draw on the canvas using the mouse, select different colors, adjust the brush size, and clear the canvas when needed. The application provides a smooth and interactive experience, making it ideal for basic sketching or note-taking.

## Features
- Draw freely on the canvas using the mouse.
- Choose different colors using a color picker.
- Adjust the brush size using a slider.
- Clear the canvas with a button click.
- Smooth and interactive drawing experience with anti-aliasing.

## Screenshot

## Requirements
Make sure you have the following installed:
- Python (3.x)
- `uv` package manager (for managing dependencies)
- Required Python dependencies:
  - PyQt6

## Installation

Follow these steps to set up the project:

1. **Initialize the project with `uv`**
   ```sh
   uv init
   ```
   This will create a `pyproject.toml` file for managing dependencies.

2. **Add dependencies**
   ```sh
   uv add pyqt6
   ```
   This will install `PyQt6` and create a virtual environment automatically.

3. **Activate the virtual environment** (optional, but useful if you want to run commands in the same environment)
   ```sh
   uv venv
   ```
   Then, activate the virtual environment:
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

## Running the Application
To launch the PyQt6 Drawing App, use the following command:
```sh
uv run python main.py
```
This ensures the script runs within the virtual environment managed by `uv`.

## Project Structure
```
├── main.py          # Main application script
├── README.md        # Project documentation
├── pyproject.toml   # Dependencies managed by uv
├── .venv/           # Automatically created virtual environment
```

## Usage
- Open the application by running `uv run python main.py`.
- Click and drag the mouse to draw on the canvas.
- Click the **Choose Color** button to change the brush color.
- Adjust the brush size using the slider.
- Click **Clear** to erase the drawing.

## License
This project is open-source and available for modification and distribution.

## Author
Developed by Muzaffar Ahmed.

