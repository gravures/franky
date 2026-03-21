# Franky Agent Guidelines

This file provides development guidelines for agentic coding assistants.

## Project Structure

This is a python monorepo managed with `Pdm` and using `uv` as a backend
to manage dependencies and workspaces.

- **Source Code**:
  - `src/` - Contains modules for the main library (the root workspace package)
  - `packages/` - Contains all workspace packages
  - `pyproject.toml` - Is the main project definitions files
- **Tests**: `tests/`
- **Dependencies**: Managed with `pdm` and `uv`. See `pyproject.toml` and `uv.lock`.

## Build, Lint, and Test

- **Build**: `pdm build_`
- **Lint**: `pdm run ruff check .`
- **Format**: `pdm run ruff format .`
- **Install/Sync Dependencies:** `pdm sync_`
- **Type Checking:** `pdm test-types`

## Code Style

- **Formatting**: We use `ruff` for formatting defined in `ruff.toml`.
- **Imports**: Imports will be sorted using `ruff` Formatting.
- **Types**: The project is fully typed and checked with `basedpyright`.
- **Naming Conventions**: Follow `PEP 8` naming conventions.
- **Error Handling**: Use standard Python error handling.
- **Docstrings**: Google-style docstrings are required.
- **Commits**: Commit messages must follow the Conventional Commits specification.
