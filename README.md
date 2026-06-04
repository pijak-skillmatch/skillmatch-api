# SkillMatch AI API

Backend API untuk SkillMatch AI yang menyediakan:

- Industry Recommendation
- Skill Gap Recommendation
- Learning Path Recommendation
- Explainable AI Recommendation

Dibangun menggunakan FastAPI dan terintegrasi dengan model Machine Learning yang telah dilatih pada repository SkillMatch ML.

---

## Features

### Industry Recommendation

Memprediksi industri yang paling sesuai berdasarkan skill dan level pengalaman pengguna.

Contoh:

Input:

```json
{
  "skills": ["Python", "SQL"],
  "experience": "Entry Level"
}
```

Output:

```json
{
  "industry": "Software",
  "probability": 0.75
}
```

---

### Skill Gap Recommendation

Mengidentifikasi skill yang perlu dipelajari untuk meningkatkan kecocokan terhadap industri target.

Contoh:

```json
["AWS", "React", "Machine Learning"]
```

---

### Learning Path Recommendation

Menyusun roadmap pembelajaran berdasarkan level skill.

Contoh:

```json
[
  {
    "level": "Intermediate",
    "skills": ["React", "Java"]
  },
  {
    "level": "Advanced",
    "skills": ["AWS", "Machine Learning"]
  }
]
```

---

### Explainable AI

Menjelaskan alasan mengapa suatu skill direkomendasikan.

Contoh:

```json
{
  "skill": "AWS",
  "reasons": ["Appears in 50.4% of Software profiles", "Strong association with Python"]
}
```

---

## Project Structure

```text
skillmatch-api/

├── app/
│   ├── api/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── artifacts/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Create environment:

```bash
conda create -n skillmatch-api python=3.11
conda activate skillmatch-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn main:app --reload
```

API Documentation:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /api/v1/health
```

### Debug Artifacts

```http
GET /api/v1/debug/artifacts
```

### Analyze Profile

```http
POST /api/v1/analyze
```

Request:

```json
{
  "skills": ["Python", "SQL"],
  "experience": "Entry Level"
}
```

---

## Tech Stack

- FastAPI
- Pydantic
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## License

Capstone Project – SkillMatch AI
