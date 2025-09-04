# Flask Guessing Game

A simple **number guessing game** built with Flask.  
You try to guess the secret number (between 1 and 100) chosen randomly by the computer.


website:https://guessing-game-tp35.onrender.com 


## 🎮 How to Play
1. Open the game in your browser.
2. Enter a number between **1 and 100**.
3. The app will tell you if your guess is:
   - ⬆️ Too low
   - ⬇️ Too high
   - 🎉 Correct!
4. Keep guessing until you find the secret number.
5. The game tracks how many attempts you made.
6. Start a new game anytime with the **Reset** button.


## 🚀 Quickstart (Local)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# visit http://localhost:5000
