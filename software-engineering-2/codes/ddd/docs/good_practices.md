# Good Practices Applied

This document describes the software engineering and coding good practices applied throughout this project.

---

## 1. Domain-Driven Design (DDD) Layered Architecture

The project is organized into four explicit layers, each with a single responsibility:

| Layer | Folder | Responsibility |
|---|---|---|
| **Domain** | `domains/` | Business entities as Pydantic models — data contracts |
| **Repository** | `repositories/` | All database access logic (SQLAlchemy ORM) |
| **Service** | `services/` | Business rules, validation, orchestration |
| **Application** | `applications/` | HTTP interface — FastAPI routers only |

**Why it matters:** Each layer depends only on the layer below it. The HTTP layer never touches the database directly, and the repository layer never contains business rules. This makes each layer independently testable and replaceable.

---

## 2. Dependency Injection

Services and repositories are injected into FastAPI route handlers using `Depends()`:

```python
def get_service(db: Session = Depends(pg.get_db)) -> StadiumService:
    return StadiumService(StadiumsRepository(db))

@router.get("/get_all")
def get_all(services: StadiumService = Depends(get_service)):
    return services.get_all()
```

**Why it matters:** Route handlers never instantiate their own dependencies. This decouples the HTTP layer from concrete implementations, simplifies mocking in tests, and manages the database session lifecycle automatically.

---

## 3. Repository Pattern

All data access is encapsulated in repository classes. No raw SQL or ORM queries appear in services or routers.

```python
class StadiumsRepository:
    def __init__(self, db: Session): ...
    def get_all(self) -> List[StadiumOut]: ...
    def get_by_id(self, id: int) -> Optional[StadiumOut]: ...
    def create(self, stadium: StadiumBase) -> StadiumOut: ...
    def update(self, id: int, stadium: StadiumBase) -> Optional[StadiumOut]: ...
    def delete(self, id: int) -> bool: ...
```

**Why it matters:** Switching from PostgreSQL to another database only requires a new repository implementation — no changes to services or routers.

---

## 4. Pydantic for Input Validation and Serialization

All input/output data is modeled with Pydantic. Input is validated at the boundary before reaching any business logic:

- `StadiumBase` — input model (no `id`, no `created_at`)
- `StadiumOut` — output model (includes `id`, `created_at`, ORM-compatible)
- `PlayerIn` — includes `team_id` for FK binding
- `PlayerOut` — safe read model

`Config: from_attributes = True` enables direct ORM-to-Pydantic conversion without manual mapping.

**Why it matters:** Prevents malformed data from reaching the database. Separating input and output models avoids accidental data leaks and simplifies API evolution.

---

## 5. Environment-Based Configuration

Secrets and environment-specific values are never hardcoded. They are loaded from `.env` using `pydantic-settings`:

```python
class DBSettings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    ...
    model_config = SettingsConfigDict(env_file=".env")
```

A `.env.example` file is committed to document required variables without exposing values.

**Why it matters:** Follows the [12-Factor App](https://12factor.net/config) principle. The same codebase runs in development, staging, and production by changing only environment variables.

---

## 6. Single Responsibility Principle (SRP)

Each class and module has one reason to change:

- `StadiumsRepository` → only changes if the database schema or ORM changes
- `StadiumService` → only changes if business rules change
- `stadiums_app.py` → only changes if the HTTP contract changes

**Why it matters:** Reduces the risk that a change in one concern breaks another.

---

## 7. ORM Relationships Declared Explicitly

SQLAlchemy relationships are declared on the ORM models:

```python
class TeamModel(Base):
    players = relationship("PlayerModel", back_populates="team")

class PlayerModel(Base):
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    team = relationship("TeamModel", back_populates="players")
```

**Why it matters:** Eager/lazy loading is handled by SQLAlchemy. The `TeamOut` model automatically includes nested `players` when serialized.

---

## 8. Input Guards in the Service Layer

Business validation lives in services, not in repositories or routers:

```python
def get_by_id(self, id: int) -> Optional[StadiumOut]:
    if id <= 0:
        raise ValueError("Stadium ID cannot be negative.")
    return self.__repo.get_by_id(id)

def create(self, stadium: StadiumBase) -> StadiumOut:
    if stadium.capacity <= 0:
        raise ValueError("Stadium capacity cannot be negative.")
    return self.__repo.create(stadium)
```

**Why it matters:** Business rules are centralized and reusable regardless of how the service is called (HTTP, CLI, test).

---

## 9. Consistent Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Files | `snake_case` | `stadiums_repository.py` |
| Classes | `PascalCase` | `StadiumsRepository` |
| Methods | `snake_case` | `get_by_id` |
| Private attributes | `__double_underscore` | `self.__db`, `self.__repo` |
| URL paths | `snake_case` | `/get_by_id/{id}` |

**Why it matters:** Consistency reduces cognitive load when reading or navigating code.

---

## 10. Package `__init__.py` as Explicit Public API

Each package exposes only what it needs to:

```python
# repositories/__init__.py
from .stadiums_repository import StadiumsRepository
from .teams_repository import TeamsRepository
from .players_repository import PlayersRepository
from .db_connection import Base, PGConn
```

Consumers import from the package name, not from internal module paths.

**Why it matters:** Internal refactoring (renaming files, moving classes) does not break imports in other layers.

---

## 11. Poetry for Dependency Management

Dependencies are declared with pinned minor versions (`^`) in `pyproject.toml`. Development tools (`ruff`, `pylint`, `pytest`, `black`) are isolated in `[dependency-groups] dev` and not installed in production.

**Why it matters:** Reproducible installs. Production images stay lean.

---

## 12. Separation of ORM and Domain Models

SQLAlchemy ORM models (`repositories/orm/`) and Pydantic domain models (`domains/`) are intentionally separate:

- ORM models define the database structure
- Domain models define the API contract

They are linked only at the repository boundary via `from_attributes = True`.

**Why it matters:** The database schema can evolve without breaking the API contract, and vice versa.
