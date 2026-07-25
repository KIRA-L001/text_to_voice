# text_to_voice

A Flask web app that extracts text from an uploaded image (OCR), translates
it into a chosen language, and converts the result into speech audio.

## How it works

1. **Upload** — drop an image on the `/upload` page (Flask-Dropzone).
2. **OCR** — the server reads the image with OpenCV and extracts text using
   Tesseract (`pytesseract`).
3. **Translate** — the detected text is shown on `/decoded`, where you pick a
   target language (100+ supported via `googletrans`).
4. **Listen** — the translated text is synthesized with Google Text-to-Speech
   (`gTTS`) and played back / downloadable in the browser.

## Project structure

```
run.py                  # App entry point
application/
  __init__.py           # Flask app factory, config, session + dropzone setup
  routes.py             # / , /upload , /decoded views
  forms.py              # WTForms form (text + language select)
  utils.py              # Language detection, translation, language map
  templates/            # Jinja2 templates
  static/               # Images and generated audio files
```

## Setup

Prerequisites: Python 3.8+, [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
installed on the system (the path is configured in `application/routes.py`).

```bash
pip install -r requirements.txt
python run.py
```

Then open http://127.0.0.1:5000.

Set the session secret via environment variable in production:

```bash
export SECRET_KEY="your-random-secret"
```

## Deployment

A `Procfile` is included for gunicorn-based hosts:

```
web: gunicorn run:app
```

## License

MIT — see [LICENSE](LICENSE).
