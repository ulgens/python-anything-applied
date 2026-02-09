<div align="center">

# python-anything

[![Python](https://img.shields.io/badge/python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/-uv-DE5FE9?logo=uv&labelColor=555)](https://github.com/astral-sh/uv)
[![prek](https://img.shields.io/badge/-prek-F54327?logo=prek&labelColor=555)](https://github.com/j178/prek)
[![Ruff](https://img.shields.io/badge/-ruff-D7FF64?logo=ruff&labelColor=555)](https://github.com/astral-sh/ruff)
[![Renovate](https://img.shields.io/badge/-renovate-308BE3?logo=renovate&labelColor=555)](https://github.com/renovatebot/renovate)

[![Git Hooks](https://img.shields.io/github/actions/workflow/status/ulgens/python-anything-applied/git-hooks.yml?logo=github&label=Git%20Hooks)](https://github.com/ulgens/python-anything-applied/actions/workflows/git-hooks.yml)

</div>

Python project starter

This repository demonstrates modern Python development best practices and serves as a template for starting new Python projects. It showcases integration of industry-standard tools and workflows.

## Key Features
- **Modern Package Management**: Uses [uv](https://github.com/astral-sh/uv) for fast, reliable dependency management
- **Code Quality**: Configured with [ruff](https://github.com/astral-sh/ruff) for linting and formatting with 45+ rule categories
- **Git Hooks**: Automated pre-commit checks via [prek](https://prek.j178.dev/)
- **CI/CD**: GitHub Actions workflows for testing and validation
- **Type Safety**: Type hints and strict configuration ready
- **Testing**: pytest with xdist for parallel test execution

## Dependencies Note
The project includes several popular Python frameworks as demonstration examples:
- **apache-airflow**: Workflow orchestration platform
- **django**: Web framework
- **fastapi**: Modern API framework
- **langchain**: LLM application framework
- **numpy**: Scientific computing
- **pandas**: Data analysis

These dependencies serve as examples for the template. Remove unused dependencies before starting your actual project.

## Required tools
- [prek](https://prek.j178.dev/installation/)

## Implemented Methods & Patterns
* ruff: ruff checks are run as git hooks and wrapped in CI. Configuration is in `ruff.toml`.

## Contribution
- Install git hooks by `prek install` and ensure your changes pass the checks before creating a pull request.
  - After `prek install`, git hooks will be automatically run while committing. To manually run the checks, use `prek run`.
