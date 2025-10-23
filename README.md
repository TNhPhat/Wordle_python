# Wordle Python

### Faculty of Information Technology  
**University of Science – VNUHCM**  
**Course:** Computational Thinking Lab  
**Author:** Trương Nhật Phát  
**Language:** Python (Pygame)

---

## Project Overview
This is a Python implementation of the popular word-guessing game **Wordle**, built with **Pygame**.  
The project enhances the original gameplay with **animations and responsive UI scaling**, providing a smooth and immersive user experience.

---

## Features
- **Core Wordle Gameplay** — Guess the 5-letter word within 6 attempts.  
- **Visual Effects** — Flip, bounce, shake, and zoom animations for letters.   
- **Smart Game Engine** — Singleton design ensures consistent game state.  
- **Responsive Interface** — UI scales dynamically with window resizing or fullscreen.  
---

## Project Structure
```
    Wordle_python/
    ├── assets/
    │ ├── fonts/
    │ ├── images/
    │ ├── wordlist/
    ├── src/
    │ ├── engine/
    │ │ └── game_engine.py 
    │ ├── graphics/
    │ │ ├── square.py 
    │ │ ├── square_table.py 
    │ │ ├── keyboard.py 
    │ │ └── play_scene.py 
    │ ├── environment/
    │ │ └── settings.py 
    │ └── main.py 
    │
    ├── requirements.txt
    └── README.md
```
## Requirements
The game need to install **Python 3.13.9** and **Pygame 2.6.1** 
## How to run game
### Prepare 
Assets folder can be downloaded from the link below:

Assets Drive: [Assets Drive link](https://drive.google.com/drive/folders/1TtcNBcTebQVegtwZSQJlgWzHZzaQU9sD?usp=sharing)

After downloading, extract and place all assets folders into:
```
Wordle_python/
```
The folder structure should look like:
```
Wordle_python/
├── assets/
│ ├── fonts/
│ ├── images/
│ ├── wordlist/
│ ├── ...
├── src/
│ ├── ...
```
### Run the game
Open the terminal and run main.py file
```
cd src
python main.py
```
