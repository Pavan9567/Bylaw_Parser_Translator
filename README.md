# 🏗️ Bylaw Section Parser & Translator

A full-stack web application that extracts structured sections from zoning bylaw PDFs and translates complex legal text into clear, plain-English rules.

This project implements a **two-step processing pipeline** with a web interface and downloadable JSON outputs.

---

## ✨ Features

### Step 1 — Extraction
- Upload zoning bylaw PDF
- Extract:
  - Section numbers (e.g. `2.2.1`)
  - Parent section hierarchy
  - Section titles
  - Full section body text (preserving bullets)
  - Start and end page numbers
- Filters out:
  - Table values
  - Numeric rows
  - Paragraph numbers that are not real section IDs

### Step 2 — Semantic Translation
- Converts legal text into:
  - `description` (plain English summary)
  - `condition_english`
  - `requirement_english`
  - `exception` (when applicable)
- Batched translation for speed
- Deterministic output (temperature = 0)

### Web Interface
- Simple React UI
- View extracted JSON
- View translated JSON
- Download JSON files for both steps

---

## 🧱 Tech Stack

### Backend
- Python 3.10+
- FastAPI
- pdfplumber (PDF parsing)
- OpenAI API (LLM translation)
- python-dotenv

### Frontend
- React (Vite)
- Axios
- react-json-pretty
- Plain CSS

---

---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create Virtual Environment

```bash
cd backend
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate


---

2️⃣ Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

---

Environment Variables

Create a .env file inside the backend/ directory:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

Notes:

Do not wrap the key in quotes

Do not commit .env to GitHub

Restart backend after changing .env



---

Run Backend Server

uvicorn app.main:app --reload

Backend runs at:

http://127.0.0.1:8000

Swagger API docs:

http://127.0.0.1:8000/docs


---

Frontend Setup (React)

Install Dependencies

cd frontend
npm install

Additional packages:

npm install axios react-json-pretty


---

Run Frontend

npm run dev

Frontend runs at:

http://localhost:5173


---
```

Application Flow

1. Open frontend in browser


2. Upload zoning bylaw PDF


3. Click Extract Sections


4. View extracted JSON (Step 1)


5. Click Translate Sections


6. View translated JSON (Step 2)


7. Download JSON outputs




---

Translation Design

Sections are translated in batches (not one-by-one)

Only sections with meaningful body text are sent to the LLM

Model used: gpt-4o-mini

Temperature: 0 (stable, deterministic JSON)

JSON is parsed safely using json.loads (no eval)



---

Known Limitations

PDF parsing is heuristic-based and may not be perfect for all layouts

Multi-column PDFs can introduce edge cases

Some informational sections are intentionally skipped

Large PDFs may take ~10–20 seconds to translate



---

Security Notes

OpenAI API key is stored only in backend

.env is excluded via .gitignore

No secrets are exposed to frontend

API calls are server-side only



---

Deployment (Optional)

Backend: Render / Railway

Frontend: Vercel / Netlify
