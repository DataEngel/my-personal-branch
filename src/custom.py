import os
from pathlib import Path

from flask import Flask, abort, send_from_directory


BASE_DIR = Path(__file__).resolve().parent.parent
PAGES = {"index.html", "about.html", "category.html", "work.html", "games.html"}
PUBLIC_DIRECTORIES = {"css", "images", "js"}

app = Flask(__name__, static_folder=None)


@app.get("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/<path:requested_path>")
def public_file(requested_path: str):
    path_parts = Path(requested_path).parts
    if requested_path in PAGES or (path_parts and path_parts[0] in PUBLIC_DIRECTORIES):
        return send_from_directory(BASE_DIR, requested_path)
    abort(404)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1",
    )
