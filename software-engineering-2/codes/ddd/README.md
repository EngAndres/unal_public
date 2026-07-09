# UNAL World Cup — Backend API

A RESTful backend built with **FastAPI** and **SQLAlchemy** following **Domain-Driven Design (DDD)** layered architecture. It manages the three main entities of a soccer World Cup system: **Stadiums**, **Teams**, and **Players**.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Requirements](#requirements)
3. [Environment Configuration](#environment-configuration)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
6. [API Reference](#api-reference)
7. [Development Tools](#development-tools)
8. [Architecture](#architecture)

---

## Project Structure

```
ddd/
├── main.py                        # Application entry point
├── pyproject.toml                 # Dependency and project manifest
├── .env                           # Local environment variables (not committed)
├── .env.example                   # Template for environment variables
│
├── config/
│   └── db_config.py               # Database settings via pydantic-settings
│
├── domains/                       # Pydantic models (business entities)
│   ├── stadiums.py                # StadiumBase, StadiumOut
│   └── teams.py                   # PlayerBase, PlayerIn, PlayerOut, TeamBase, TeamOut
│
├── repositories/                  # Data access layer (SQLAlchemy)
│   ├── db_connection.py           # Engine, session factory, Base
│   ├── stadiums_repository.py     # CRUD for stadiums
│   ├── teams_repository.py        # CRUD for teams
│   ├── players_repository.py      # CRUD for players
│   └── orm/
│       ├── stadium.py             # StadiumModel ORM
│       ├── team.py                # TeamModel ORM
│       └── player.py              # PlayerModel ORM
│
├── services/                      # Business logic layer
│   ├── stadiums_service.py        # StadiumService
│   ├── teams_service.py           # TeamService
│   └── players_service.py         # PlayerService
│
├── applications/                  # API routers (FastAPI)
│   ├── stadiums_app.py            # /stadiums endpoints
│   ├── teams_app.py               # /teams endpoints
│   └── players_app.py             # /players endpoints
│
├── architecture/
│   └── architecture.drawio        # System architecture diagram
│
└── docs/
    ├── good_practices.md          # Design and coding good practices applied
    └── troubleshooting.md         # Common issues and solutions
```

---

## Requirements

### Runtime

| Package | Version | Purpose |
|---|---|---|
| `fastapi` | `^0.136.0` | Web framework and OpenAPI generation |
| `uvicorn` | `^0.44.0` | ASGI server to run FastAPI |
| `pydantic` | `^2.13.3` | Data validation and serialization |
| `pydantic-settings` | `^2.14.0` | Environment-based configuration |
| `sqlalchemy` | `^2.0.49` | ORM and database abstraction |
| `psycopg2-binary` | `^2.9.12` | PostgreSQL adapter for Python |
| `python-dotenv` | `^1.2.2` | Load `.env` files into environment |

### Development

| Package | Version | Purpose |
|---|---|---|
| `ruff` | `^0.15.11` | Fast Python linter |
| `pylint` | `^4.0.5` | Static code analysis |
| `pytest` | `^9.0.3` | Testing framework |
| `black` | `^26.3.1` | Code formatter |

### System

- **Python** `>= 3.12`
- **PostgreSQL** `>= 14` (running and accessible)
- **Poetry** `>= 2.0.0` (dependency manager)

---

## Environment Configuration

Copy the example file and fill in your PostgreSQL credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
DB_USERNAME=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=worldcup
```

> The `DATABASE_URL` is assembled automatically as:  
> `postgresql://<DB_USERNAME>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>`

---

## Installation

### 1. Clone and enter the project

```bash
git clone <repository-url>
cd ddd
```

### 2. Install Poetry (if not installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Install all dependencies

```bash
poetry install
```

This installs both runtime and development dependencies. To install runtime only:

```bash
poetry install --only main
```

### 4. Create the database schema

The ORM models use SQLAlchemy's `Base.metadata`. To create all tables, run a one-time script or extend `main.py`:

```python
from repositories.db_connection import Base, PGConn
from repositories.orm import StadiumModel, TeamModel, PlayerModel

pg = PGConn()
# Call create_all with the engine directly:
from sqlalchemy import create_engine
from config import db_settings
engine = create_engine(db_settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)
```

Alternatively, use a migration tool like **Alembic** for production environments.

---

## Running the Application

### Development mode (with auto-reload)

```bash
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production mode

```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

Once running, the interactive API docs are available at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health check**: [http://localhost:8000/](http://localhost:8000/)

---

## API Reference

### Stadiums — `/stadiums`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/stadiums/get_all` | List all stadiums |
| `GET` | `/stadiums/get_by_id/{id}` | Get a stadium by ID |
| `POST` | `/stadiums/add` | Create a new stadium |
| `PUT` | `/stadiums/update/{id}` | Update an existing stadium |
| `DELETE` | `/stadiums/delete/{id}` | Delete a stadium |

**StadiumBase payload:**
```json
{
  "name": "Estadio El Campín",
  "capacity": 36343,
  "address": "Cra. 30 #57-60",
  "city": "Bogotá"
}
```

---

### Teams — `/teams`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/teams/get_all` | List all teams |
| `GET` | `/teams/get_by_id/{id}` | Get a team by ID |
| `POST` | `/teams/add` | Create a new team |
| `PUT` | `/teams/update/{id}` | Update an existing team |
| `DELETE` | `/teams/delete/{id}` | Delete a team |

**TeamBase payload:**
```json
{
  "name": "Colombia",
  "color": "yellow"
}
```

---

### Players — `/players`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/players/get_all` | List all players |
| `GET` | `/players/get_by_id/{id}` | Get a player by ID |
| `GET` | `/players/get_by_team/{team_id}` | List all players of a team |
| `POST` | `/players/add` | Create a new player |
| `PUT` | `/players/update/{id}` | Update an existing player |
| `DELETE` | `/players/delete/{id}` | Delete a player |

**PlayerIn payload:**
```json
{
  "name": "James Rodríguez",
  "age": 33,
  "weight": 75.0,
  "height": 1.80,
  "team_id": 1
}
```

---

## Development Tools

### Linting

```bash
poetry run ruff check .
poetry run pylint applications/ services/ repositories/ domains/
```

### Formatting

```bash
poetry run black .
```

### Testing

```bash
poetry run pytest
```

---

## Architecture

See the architecture diagram at [architecture/architecture.drawio](architecture/architecture.drawio).

The system follows a four-layer DDD structure:

```
[ HTTP Client ]
      ↓
[ Applications ]  — FastAPI routers, HTTP interface
      ↓
[   Services   ]  — Business logic, validation rules
      ↓
[ Repositories ]  — Data access, SQLAlchemy ORM
      ↓
[  PostgreSQL   ]  — Persistent data store
```

Domain models (Pydantic) are shared across layers as data contracts.

---

*Author: Prof. Carlos Andres Sierra — casierrav@unal.edu.co*  
*License: GNU/GPL 3*
