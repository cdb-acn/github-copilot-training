# Testing Standards for this FastAPI Project

## Directory Structure
- Separate `unit/` and `integration/` subdirectories under `tests/`.
- All tests must live inside the `tests/` directory.
- Include `conftest.py` for shared fixtures (app, client, db_session, auth_token).

## Naming Conventions
- Unit test files: `test_<module>.py` (e.g., `app/main.py` → `tests/unit/test_main.py`).
- Integration test files: `test_<module>.py` (e.g., endpoints in `app/main.py` → `tests/integration/test_main.py`).
- Test function names: `def test_<target>_<expected_behavior>()`.

## Unit Testing Guidelines
- Test one function or class in isolation.
- Mock external dependencies when needed.
- Use `pytest.raises` for exception testing.
- Example (indented, no fenced block):
    def test_myfunc_raises_on_invalid_input():
        with pytest.raises(ValueError):
            myfunc(None)

## Integration Testing Guidelines
- Use `httpx.AsyncClient` for endpoint tests.
- Mark integration tests with `@pytest.mark.integration`.
- Assert status codes, JSON structures, and endpoint behavior.
- Example (indented, no fenced block):
    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_items_create_returns_201(client):
        resp = await client.post('/item/create', json={...})
        assert resp.status_code == 201

## API Testing Requirements
- Cover happy path, validation errors, and failure cases.
- Validate responses against Pydantic models in `app/models.py`.
- Ensure async endpoints are awaited correctly.

## Fixtures
- Provide `app`, `client`, `db_session`, and `auth_token` fixtures in `tests/conftest.py`.
- Reuse fixtures across tests to keep tests fast and deterministic.

## Agent Behavior Rules
- Generated tests must follow the rules above.
- Place files only under `tests/` and do not create files outside `tests/`.
- Include happy path, validati on, error-condition, and type-checking tests.

## Coverage
- Check coverage with `uv run pytest --cov=app tests/`.
- Aim for 85%+ coverage for changed modules; add tests if coverage is insufficient.

## Usage Examples
- Generate unit tests for a module.
- Generate integration tests for an endpoint.
- Fix missing tests according to these standards.

## Summary
- Keep unit and integration tests separate, follow naming conventions, use `httpx.AsyncClient` for integration, use fixtures from `conftest.py`, and validate API responses against Pydantic models.
