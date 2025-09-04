from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import timedelta

app = Flask(__name__)
# NOTE: Replace this with a strong random value in production
app.config['SECRET_KEY'] = 'change-me-in-production'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


def start_new_game():
    session['random_number'] = random.randint(1, 100)
    session['guesses'] = 0
    session['game_end'] = False


@app.route('/', methods=['GET'])
def index():
    # Initialize session-based game state on first visit
    if 'random_number' not in session:
        start_new_game()
    return render_template('index.html',
                           feedback=session.get('feedback'),
                           prev_guess=session.get('prev_guess'),
                           game_end=session.get('game_end', False),
                           guesses=session.get('guesses', 0))


@app.route('/guess', methods=['POST'])
def guess():
    if 'random_number' not in session:
        start_new_game()

    prev_guess = request.form.get('prev_guess')
    guess_raw = request.form.get('guess', '').strip()

    # Basic input validation
    try:
        new_guess = int(guess_raw)
    except (TypeError, ValueError):
        session['feedback'] = "❗ Invalid guess. Please enter an integer."
        session['prev_guess'] = prev_guess
        return redirect(url_for('index'))

    # Update guesses count
    session['guesses'] = session.get('guesses', 0) + 1

    random_number = session['random_number']

    if new_guess == random_number:
        session['feedback'] = f"🎉 Congratulations! You guessed it: {random_number} in {session['guesses']} tries."
        session['game_end'] = True
    elif new_guess < random_number:
        session['feedback'] = "⬆️ Too low! Try a higher number."
        session['game_end'] = False
    else:
        session['feedback'] = "⬇️ Too high! Try a lower number."
        session['game_end'] = False

    session['prev_guess'] = new_guess
    return redirect(url_for('index'))


@app.route('/reset', methods=['POST'])
def reset():
    start_new_game()
    session['feedback'] = "🔁 New game started! Guess a number between 1 and 100."
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Debug server for local development
    app.run(host='0.0.0.0', port=5000, debug=True)
