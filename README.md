# 📚 leseecke
 
**leseecke** ist dein persönliches Bücherarchiv. Speichere und bewerte Bücher oder halte deine Gedanken und Lieblingszitate direkt fest.
 
## Features
 
- **📖 Bücher verwalten** – Titel, Autor, Jahr und Genre in einer zentralen Übersicht
- **⭐ Bewertungen** – Gib jedem Werk eine Stern-Bewertung
- **📝 Notizen** – Hinterlege persönliche Gedanken, Rezensionen oder Lieblingszitate direkt zu den Büchern
 
## Tech Stack
 
| Schicht    | Technologie                          |
|-----------|--------------------------------------|
| Backend   | [FastAPI](https://fastapi.tiangolo.com/) |
| Datenbank | [SQLModel](https://sqlmodel.tiangolo.com/) |
| Server    | [Uvicorn](https://www.uvicorn.org/)  |
| Python    | 3.13+                                |
| Tooling   | [uv](https://docs.astral.sh/uv/)     |
 
## Voraussetzungen
 
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) installiert
 
## Installation & Start
 
```bash
# Repository klonen
git clone https://github.com/steven-ngle/leseecke.git
cd leseecke
 
# Abhängigkeiten installieren
uv sync
 
# Entwicklungsserver starten
uv run uvicorn backend.main:app --reload
```
 
Die API ist dann erreichbar unter `http://localhost:8000`.  
Interaktive Dokumentation (Swagger UI): `http://localhost:8000/docs`
 
## Projektstruktur
 
leseecke/
├── backend/         # FastAPI-Anwendung
├── pyproject.toml   # Projektdefinition & Abhängigkeiten
├── uv.lock          # Lockfile
└── README.md


 
