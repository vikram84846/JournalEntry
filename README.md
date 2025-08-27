# Grocery Shop API

This project is a backend API for a Grocery Shop, built using FastAPI and SQLAlchemy. The API is designed to manage various components of a grocery shop, with the first implemented component being the JournalEntry system.

## Features

- FastAPI-based RESTful API
- SQLAlchemy ORM for database operations
- Modular structure for future expansion

## Current Component

### JournalEntry

The JournalEntry module allows you to:

- Create new journal entries
- View all journal entries
- Update existing entries
- Delete entries

Each journal entry records:

- Entry date
- Debit account
- Credit account
- Amount
- Narration (optional)

## Project Structure

```
database.py
main.py
Journal/
	models.py
	routes.py
	schema.py
	__init__.py
```

## Getting Started

1. Clone the repository.
2. Install dependencies (see `pyproject.toml`).
3. Set up your environment variables (see `.env` and `database.py`).
4. Run the API server:
   ```bash
   python main.py
   ```

## Future Work

Additional components for inventory, sales, and more will be added soon.

---

This README will be updated as new features are implemented.
