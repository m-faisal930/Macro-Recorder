# Macro-Recorder
The project that will automate every task you perform on the PC

# PyMacroRecord


PyMacroRecord is a free and easy-to-use macro recorder coded in Python. It provides a GUI made with Tkinter, making it simple for users to interact with the application.

## Overview

PyMacroRecord is completely free with no ads or premium features. It offers unlimited functionality without any limitations.

## Features

- **Easy to Use: PyMacroRecord provides a straightforward interface for users to record and playback macros.
- **No Limitations**: Free without any premium purchases or limitations on features.
- **Customizable Repeats**: Users can set an infinite amount of repeats for their recorded macros.
- **Adjustable Playback Speed**: Change the speed of macro playback according to your preferences.
- **Interval in Playbacks**: Set intervals between playback actions for precise control.
- **Save and Load Records**: Save your recorded macros and load them later for reuse.
- **Universal Files**: Works with .json files for compatibility across different systems.
- **After-playback Options**: Options like standby or shutdown computer after playback.
- **Custom Hotkeys**: Set custom hotkeys for starting and stopping recording, playback, etc.
- **Record Mouse Movement, Clicks, and Keyboard Input**: Record various actions including mouse movement, clicks, and keyboard input.
- **Smooth Mouse Recording**: Provides smooth recording of mouse movements for accurate playback.

## How it Works

1. To start recording, simply press the red button.
2. Move your mouse, click, and type on your keyboard; all actions will be recorded (You can choose what will be recorded).
3. To stop the recording, click on the black square.
4. To play a recording, click on the green play icon. Press the F3 key (by default) to stop playback.

## Showcase

- [Windows Showcase](link_to_windows_showcase_video)
- [macOS Showcase](link_to_macos_showcase_video)
- [Linux Showcase](link_to_linux_showcase_video)

## Bug Reports and Updates

If you encounter a bug or want to request an update, simply create an issue [here](link_to_issue_tracker).

## Installation

For users who don't have Windows or prefer not to use the executable file:

1. Install Python if not already installed.
2. Download the latest source code release [here](link_to_source_code_release).
3. Extract the files.
4. Open the terminal and navigate to the software folder.
5. Install the required dependencies using the command `pip3 install -r requirements.txt`.
6. If you are on Linux, you might need to install Tkinter manually.
7. Remove `win10toast` from `requirements.txt` if you are not using Windows.
8. For Mac users, add Python app to accessibility settings in system preferences.
9. Finally, navigate to the `src` folder and run the command `python3 main.py`.

## Build (Windows)

To build the application for Windows, PyInstaller is used.

- For one-file output:

```
pyinstaller --noconfirm --onefile --windowed --icon "src/assets/logo.ico" --name "PyMacroRecord-portable" --contents-directory "." --upx-dir upx --add-data "src/assets;assets/" --add-data "src/hotkeys;hotkeys/" --add-data "src/macro;macro/" --add-data "src/utils;utils/" --add-data "src/windows;windows/"  "src/main.py"
```

- For one-directory output:

```
pyinstaller --noconfirm --onedir --windowed --icon "src/assets/logo.ico" --name "PyMacroRecord" --contents-directory "." --upx-dir upx --add-data "src/assets;assets/" --add-data "src/hotkeys;hotkeys/" --add-data "src/macro;macro/" --add-data "src/utils;utils/" --add-data "src/windows;windows/"  "src/main.py"
```

