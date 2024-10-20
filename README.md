# FF9 Jump Rope Jumper 🎮🏆

Welcome to the definitive solution for the Final Fantasy IX Jump Rope minigame! This tool makes mastering the jump rope challenge an absolute breeze! 😎✨

And the best part? **It works on the first try**! No more ninja reflexes required. With a finely-tuned visual and timing control system, you'll be jumping like a pro in no time. 🔥

---

## Setup

Here’s everything you need to get started:

### 1. Install Python (if you don't have it already)

If you don't have Python installed, follow these simple steps:

- **Windows**:
  1. Go to the official Python website: https://www.python.org/downloads/
  2. Download the latest version of Python (e.g., Python 3.x).
  3. Run the installer and make sure to check **"Add Python to PATH"** before clicking **"Install Now"**.

- **macOS**:
  1. Open the terminal and type:
     ```bash
     brew install python
     ```
  2. (You’ll need Homebrew installed for this command).

- **Linux**:
  1. Open a terminal and type:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

Check if Python is installed by running:
```bash
python --version
```

### 2. Install the required dependencies

The script uses some external libraries that need to be installed if you don't have them already:

- **Pillow**: A Python Imaging Library, used to manipulate and analyze images (used for the visual detection system).
- **mss**: A library to capture screenshots efficiently. It's lightweight and perfect for capturing regions of the screen.

Run the following command to install them:

```bash
python3 -m pip install -U --user Pillow mss
```

### 3. Install Memoria Mod Launcher and activate 60 FPS

To ensure this script works correctly, you need to install the **Memoria Mod Launcher** for FF9 and activate the **60 FPS** option.

1. Download and install the Memoria Launcher from this link:
   [Memoria Mod Launcher](https://github.com/Albeoris/Memoria/releases)
   
2. After installing, open the launcher and make sure the **60 FPS** option is activated.

### 4. Position the game window

- Run **Final Fantasy IX** in **windowed mode** with a resolution of **800x600**.
- Move the game window to the **top-left corner** of your screen, aligning it as closely as possible to the edges.
- Approach the jump rope minigame, and once the exclamation mark appears on screen, **don't press any buttons**.

---

## How to use the program

1. Run the script:
   From the project directory, execute:
   ```bash
   python3 rope_jumper.py
   ```

2. Return to the game window:
   The program will take control and jump automatically when the time is right.

---

## How does it work?

1. **Visual Detection**: Detects the exclamation mark on screen and presses the `X` key at the perfect moment.
2. **Backup Timing**: In case visual detection misses, the program uses a fallback timing system to ensure jumps.

---

## Libraries used

### External libraries:

1. **mss**: 
   - Captures screenshots quickly and efficiently.
   - Used for detecting the appearance of the exclamation mark in the game window.

2. **Pillow (PIL)**: 
   - Python Imaging Library for manipulating and analyzing images.
   - Converts screenshots into images for pixel analysis to detect the correct timing.

### Standard Python libraries:

1. **ctypes**: 
   - A foreign function library in Python, used to interact with Windows API and simulate key presses.

2. **time**: 
   - Used to manage timing and delays between actions, ensuring precise jump timing.

---

## Game Setup

- **Game Mode**: Windowed Mode
- **Resolution**: 800x600
- **Position**: Move the game window to the top-left corner of your screen.
- **Memoria Mod**: Make sure the **60 FPS** option is enabled in the Memoria Launcher.

---

## Credits

Thanks to:

- [Septomor](https://github.com/septomor/FF9-Jump-Rope-Script) for the original script.
- [Fritz-C](https://gist.github.com/fritz-c/7c0f5994a9bb21f4d93b58eca20882a8) for the trigger key script.
- **Andrea Alvino** for combining and improving the scripts.

---

## License

This project is licensed under the MIT License. Enjoy!

---

It works on the first try! Test it yourself and see how smooth it is! 💪✨

Happy jumping! 🤖🔧 
