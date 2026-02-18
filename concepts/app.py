"""
Minimal Flask server: serves the concepts app and persists urlCorrect to conceptsDB.json.
Run from this directory: flask --app app run
"""
import json
import os

from flask import Flask, request, send_from_directory

app = Flask(__name__)
BASE = os.path.dirname(__file__)
CONCEPTS_PATH = os.path.join(BASE, "conceptsDB.json")


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/conceptsDB.json")
def concepts_json():
    return send_from_directory(BASE, "conceptsDB.json")


@app.patch("/api/concepts/<int:index>")
def update_concept(index):
    data = request.get_json(force=True, silent=True) or {}
    url_correct = data.get("urlCorrect")
    if url_correct not in (True, False):
        return {"error": "urlCorrect must be true or false"}, 400

    with open(CONCEPTS_PATH, "r", encoding="utf-8") as f:
        concepts = json.load(f)
    if index < 0 or index >= len(concepts):
        return {"error": "index out of range"}, 404

    concepts[index]["urlCorrect"] = url_correct
    with open(CONCEPTS_PATH, "w", encoding="utf-8") as f:
        json.dump(concepts, f, indent=2, ensure_ascii=False)

    return {"ok": True}
