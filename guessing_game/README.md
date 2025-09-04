# Flask Guessing Game

A minimal Flask port of your Django number guessing game.

## Quickstart (Local)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# visit http://localhost:5000
```

## Project Structure

```
flask_guessing_game/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Notes

- Session-based game state mimics your Django version: `random_number`, `guesses`, `prev_guess`, and `game_end`.
- Replace `SECRET_KEY` in `app.py` for production.
- To deploy on a PaaS, add a `Procfile` like:
  ```
  web: gunicorn app:app
  ```
  and include `gunicorn` in `requirements.txt`.
