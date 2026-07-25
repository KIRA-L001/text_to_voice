"""Entry point for the text_to_voice Flask application.

Run locally with:  python run.py
"""

from application import app

if __name__ == "__main__":
    app.run(debug=True)
