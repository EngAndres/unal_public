# Troubleshooting Guide

This document covers common problems encountered when setting up, running, or developing this project, along with their solutions.

---

## Table of Contents

1. [Database Connection Errors](#1-database-connection-errors)
2. [Environment Variables Not Loaded](#2-environment-variables-not-loaded)
3. [Tables Do Not Exist](#3-tables-do-not-exist)
4. [Poetry / Dependency Issues](#4-poetry--dependency-issues)
5. [Uvicorn Startup Errors](#5-uvicorn-startup-errors)
6. [Pydantic Validation Errors](#6-pydantic-validation-errors)
7. [SQLAlchemy ORM / Relationship Errors](#7-sqlalchemy-orm--relationship-errors)
8. [HTTP 422 Unprocessable Entity](#8-http-422-unprocessable-entity)
9. [HTTP 500 Internal Server Error](#9-http-500-internal-server-error)
10. [Import Errors at Startup](#10-import-errors-at-startup)
11. [psycopg2 Installation Fails](#11-psycopg2-installation-fails)
12. [Running Tests Fails](#12-running-tests-fails)

---

## 1. Database Connection Errors

### Symptom
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server
```
or
```
connection refused on port 5432
```

### Causes & Solutions

**A. PostgreSQL is not running**
```bash
# macOS
brew services start postgresql@14

# Linux
sudo systemctl start postgresql
```

**B. Wrong credentials in `.env`**  
Verify the values in your `.env` file match your PostgreSQL setup:
```env
DB_USERNAME=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=worldcup
```
Test the connection directly:
```bash
psql -U postgres -h localhost -p 5432 -d worldcup
```

**C. The database does not exist**
```bash
psql -U postgres -c "CREATE DATABASE worldcup;"
```

---

## 2. Environment Variables Not Loaded

### Symptom
```
pydantic_settings.env_settings.EnvSettingsError: ...
ValidationError: DB_USERNAME field required
```

### Causes & Solutions

**A. `.env` file is missing**
```bash
cp .env.example .env
# Then fill in your values
```

**B. Running from the wrong directory**  
`pydantic-settings` looks for `.env` relative to the working directory. Always run `uvicorn` from the project root (the folder containing `.env`):
```bash
cd /path/to/ddd
poetry run uvicorn main:app --reload
```

**C. Variable names have extra spaces**  
Ensure `.env` has no spaces around `=`:
```env
# Correct
DB_HOST=localhost

# Wrong
DB_HOST = localhost
```

---

## 3. Tables Do Not Exist

### Symptom
```
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "stadiums" does not exist
```

### Solution

Tables must be created before the application can use them. Run this once:

```python
# In a Python shell or a separate script
import sys
sys.path.insert(0, '.')

from config import db_settings
from sqlalchemy import create_engine
from repositories.db_connection import Base
from repositories.orm import StadiumModel, TeamModel, PlayerModel  # ensure all models are imported

engine = create_engine(db_settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)
print("Tables created.")
```

Or add this block temporarily to `main.py` startup:
```python
from repositories.db_connection import Base
from repositories.orm import StadiumModel, TeamModel, PlayerModel
from sqlalchemy import create_engine
from config import db_settings

engine = create_engine(db_settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)
```

> For production environments, use **Alembic** for managed migrations.

---

## 4. Poetry / Dependency Issues

### Symptom
```
ModuleNotFoundError: No module named 'fastapi'
```
or Poetry commands fail.

### Solutions

**A. Dependencies not installed**
```bash
poetry install
```

**B. Running Python outside the Poetry environment**  
Always prefix commands with `poetry run`:
```bash
poetry run uvicorn main:app --reload
poetry run pytest
```
Or activate the virtual environment first:
```bash
poetry shell
uvicorn main:app --reload
```

**C. Poetry itself not found**
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
# Add to PATH (add to your shell profile)
export PATH="$HOME/.local/bin:$PATH"
```

**D. Python version mismatch**  
The project requires Python `>=3.12`. Check:
```bash
python3 --version
poetry env use python3.12
poetry install
```

---

## 5. Uvicorn Startup Errors

### Symptom
```
ERROR: Error loading ASGI app. Could not import module "main".
```

### Solution

Run uvicorn from the directory containing `main.py`:
```bash
cd /path/to/ddd
poetry run uvicorn main:app --reload
```

If you see port already in use:
```bash
# Find and kill the process on port 8000
lsof -ti:8000 | xargs kill -9
```

---

## 6. Pydantic Validation Errors

### Symptom
Endpoint returns:
```json
{"detail": [{"type": "missing", "loc": ["body", "capacity"], "msg": "Field required"}]}
```

### Solution

Check the expected request body in the Swagger docs at `http://localhost:8000/docs`. Ensure your request includes all required fields. For example, `POST /stadiums/add` requires:
```json
{
  "name": "string",
  "capacity": 0,
  "address": "string",
  "city": "string"
}
```

---

## 7. SQLAlchemy ORM / Relationship Errors

### Symptom
```
sqlalchemy.exc.InvalidRequestError: When initializing mapper ... could not assemble any primary key columns
```
or
```
NoReferencedTableError: Foreign key associated with column 'players.team_id' could not find table 'teams'
```

### Solution

Ensure all ORM models are imported before `Base.metadata.create_all()` is called. SQLAlchemy needs to know about all models to resolve relationships:

```python
# This must import ALL models before create_all
from repositories.orm import StadiumModel, TeamModel, PlayerModel
Base.metadata.create_all(bind=engine)
```

Also ensure the `teams` table is created **before** `players` (foreign key constraint). `create_all` handles this automatically if all models are imported.

---

## 8. HTTP 422 Unprocessable Entity

### Symptom
The API returns 422 when sending a request.

### Diagnosis

1. Open `http://localhost:8000/docs` and use the Swagger UI to test the endpoint.
2. Check the response body — it includes a detailed `detail` array showing exactly which fields failed validation and why.
3. Common causes:
   - Sending a string where an integer is expected (`"age": "thirty"`)
   - Missing required fields
   - Negative or zero values rejected by service-layer guards

---

## 9. HTTP 500 Internal Server Error

### Symptom
Endpoint returns a generic 500 error.

### Diagnosis

Check the terminal running uvicorn. The full Python traceback is printed there. Common causes:

| Cause | Fix |
|---|---|
| Database not reachable | See [Section 1](#1-database-connection-errors) |
| Table does not exist | See [Section 3](#3-tables-do-not-exist) |
| `ValueError` raised in service | Check service-layer validation — add error handling to router if needed |
| SQLAlchemy session not closed | This is handled automatically by `PGConn.get_db()` via `finally: db.close()` |

To get better error details in development, add FastAPI's exception handler or enable debug mode:
```python
app = FastAPI(debug=True)
```

---

## 10. Import Errors at Startup

### Symptom
```
ImportError: cannot import name 'TeamIn' from 'domains'
```

### Solution

The domain models were refactored. `TeamIn` was replaced by `TeamBase`. Check [domains/__init__.py](../domains/__init__.py) to see the current exported names:

```python
from .teams import PlayerBase, PlayerIn, PlayerOut, TeamBase, TeamOut
```

Update any code referencing the old `TeamIn` or `Player` names.

---

## 11. psycopg2 Installation Fails

### Symptom
```
Error: pg_config executable not found.
```

### Solution

Use the binary version (already declared in `pyproject.toml` as `psycopg2-binary`). If you see this error, ensure you're installing via Poetry:

```bash
poetry install
```

If building from source is required:
```bash
# macOS
brew install postgresql

# Ubuntu/Debian
sudo apt-get install libpq-dev python3-dev
```

---

## 12. Running Tests Fails

### Symptom
```
ModuleNotFoundError: No module named 'applications'
```

### Solution

Pytest must be run from the project root so that Python can resolve the package imports:

```bash
cd /path/to/ddd
poetry run pytest
```

If you have a `conftest.py`, ensure it adds the project root to `sys.path`:

```python
# conftest.py
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
```

---

## Quick Reference

| Problem | Section |
|---|---|
| Can't connect to database | [1](#1-database-connection-errors) |
| `.env` variables not found | [2](#2-environment-variables-not-loaded) |
| Table does not exist | [3](#3-tables-do-not-exist) |
| `ModuleNotFoundError` | [4](#4-poetry--dependency-issues), [10](#10-import-errors-at-startup) |
| Port already in use | [5](#5-uvicorn-startup-errors) |
| Request validation error | [6](#6-pydantic-validation-errors), [8](#8-http-422-unprocessable-entity) |
| ORM relationship error | [7](#7-sqlalchemy-orm--relationship-errors) |
| 500 server error | [9](#9-http-500-internal-server-error) |
| psycopg2 fails to install | [11](#11-psycopg2-installation-fails) |
| Tests can't find modules | [12](#12-running-tests-fails) |
