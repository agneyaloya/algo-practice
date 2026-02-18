# Concepts app

A simple browser UI to read and review concept notes. Data lives in `conceptsDB.json`; the Flask backend persists Correct/Incorrect URL flags back to that file.

---

## For AI agents: adding and maintaining concepts

### Data source

- **File:** `conceptsDB.json`
- **Shape:** JSON array of concept objects. Order = display order (TOC and prev/next).

### Concept object schema

| Field        | Type    | Required | Description |
|-------------|---------|----------|-------------|
| `date`      | string  | yes      | Human-readable date/time, e.g. `"Feb 18, 10.11 am"`. |
| `name`      | string  | yes      | Short title; used in TOC and as the concept heading. |
| `url`       | string  | yes      | Link for the concept (e.g. docs/source). |
| `urlCorrect`| boolean or null | yes | `true` / `false` if user marked URL correct/incorrect; `null` if not set. Persisted by the Flask app. |
| `text`      | string  | yes      | Body of the concept. Supports simple formatting (see below). |

### Adding a new concept

1. Append a new object to the array in `conceptsDB.json`.
2. Use valid JSON: escape `"` as `\"` and use `\n` for newlines inside the `text` string.
3. Set `urlCorrect` to `null` unless you have a reason to set it.

Example minimal concept:

```json
{
  "date": "Feb 18, 10.11 am",
  "name": "Concept title",
  "url": "https://example.com/docs",
  "urlCorrect": null,
  "text": "First paragraph.\n\nSecond paragraph with **bold** and `code`."
}
```

### Text formatting (concept body)

Rendered in `index.html` by `formatText()`:

- **Bold:** `**text**` → **text**
- **Inline code:** `` `code` `` → monospace, pill-style background
- **Code block:** wrap in fenced block so the parser sees it:

  ````
  ```
  $ some-command
  line two
  ```
  ````

Use these so that commands, file names, env vars, and code snippets are clearly styled. When adding or editing concepts, add backticks/code blocks where there are commands, file paths, or code.

### JSON escaping in `text`

- Newlines: `\n`
- Double quote: `\"`
- Backslash: `\\`
- Backticks and `*` do **not** need escaping.

### Maintaining existing concepts

- **Code that isn’t formatted:** Add `` ` `` for inline code (e.g. `manage.py`, `DJANGO_SETTINGS_MODULE`) and `` ``` ... ``` `` for multi-line blocks (e.g. shell commands, JSON snippets).
- **URL or title changes:** Edit `url` or `name` in the object.
- **Persistence:** Correct/Incorrect is stored in `conceptsDB.json` by the Flask backend when the user clicks the buttons; do not overwrite `urlCorrect` unless you intend to reset it.

### Running the app

- From the `concepts` directory:
  - `pip install -r requirements.txt` (prefer a venv).
  - `flask --app app run`
- Open http://127.0.0.1:5000/
- Without Flask (e.g. `python3 -m http.server` from parent): static assets work but Correct/Incorrect will not persist to the file.

### Files

| File               | Purpose |
|--------------------|---------|
| `conceptsDB.json`  | Single source of truth for concepts and URL flags. |
| `index.html`       | UI, fetches JSON and renders concepts; calls PATCH API for Correct/Incorrect. |
| `app.py`           | Flask app: serves `index.html` and `conceptsDB.json`, PATCH `/api/concepts/<index>` writes `urlCorrect` back to JSON. |
| `requirements.txt` | Flask dependency. |
