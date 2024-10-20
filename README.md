# FF9 Jump Rope Jumper 🎮🏆

Welcome to the definitive solution for the Final Fantasy IX Jump Rope minigame! This tool makes mastering the jump rope challenge an absolute breeze! 😎✨

---

## 🚨 IMPORTANT: 3 Seconds to Click the Game Window!

After starting the script, **you have exactly 3 seconds** to click on the game window. Make sure to click **inside the window once** during these 3 seconds to ensure the script can interact with the game. **If you do not click inside the game window, the script WILL NOT WORK.** 

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

2. **IMPORTANT: You have 3 seconds to click inside the game window!**
   After running the script, you must **click inside the game window once** within 3 seconds, or else the script won't work properly. This will allow the script to interact with the game and automate the jumping process.

3. Sit back and let the script do the jumping for you!

---

### Credits

This project was originally based on the work by:
- [Septomor](https://github.com/septomor/FF9-Jump-Rope-Script)
- [Fritz-C](https://gist.github.com/fritz-c/7c0f5994a9bb21f4d93b58eca20882a8)

Special thanks to the **Memoria Mod Launcher** team for their work in improving the game's performance and capabilities.

Good luck with your 1000 jumps! 💪✨
