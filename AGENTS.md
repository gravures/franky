# Franky Agent Guidelines

This file provides development guidelines for agentic coding assistants.

## Project Structure

This is a python monorepo managed with `Pdm` and using `uv` as a backend
to manage dependencies and workspaces.

- **Source Code**:
  - `src/` - Contains modules for the main library (the root workspace package)
  - `packages/` - Contains all workspace packages
  - `pyproject.toml` - Is the main project definitions files
- **Dependencies**: Managed with `uv`. See `pyproject.toml` and `uv.lock`.

## Build, Lint

`mise` is used to manage almost all the tasks on this project, run `mise tasks`
to view all available tasks.

- **Build**: `mise run build`
- **Lint**: `mise run lint [files,...]`
- **Check Format**: `mise run lint:format [files,...]`
- **Format**: `mise run code:format [files,...]`
- **Type Checking**: `mise run typecheck [files,...]`

## Code Style

- **Formatting**: We use `ruff` for formatting defined in `ruff.toml`.
- **Types**: The project is fully typed and checked with `basedpyright`.
- **Naming Conventions**: Follow `PEP 8` naming conventions.
- **Docstrings**: Google-style docstrings are required.
- **Commits**: Commit messages must follow the Conventional Commits specification.
