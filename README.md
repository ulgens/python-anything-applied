> [!WARNING]
> This repo is archived and no longer maintained. The template version of this project is available in the [python-anything](https://github.com/ulgens/python-anything) repository.

<div align="center">

# python-anything-applied

[![Python](https://img.shields.io/badge/python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/-uv-DE5FE9?logo=uv&labelColor=555)](https://github.com/astral-sh/uv)
[![prek](https://img.shields.io/badge/-prek-F54327?logo=prek&labelColor=555)](https://github.com/j178/prek)
[![Ruff](https://img.shields.io/badge/-ruff-D7FF64?logo=ruff&labelColor=555)](https://github.com/astral-sh/ruff)
[![Renovate](https://img.shields.io/badge/-renovate-308BE3?logo=renovate&labelColor=555)](https://github.com/renovatebot/renovate)

[![Git Hooks](https://img.shields.io/github/actions/workflow/status/ulgens/python-anything-applied/git-hooks.yml?logo=github&label=Git%20Hooks)](https://github.com/ulgens/python-anything-applied/actions/workflows/git-hooks.yml)

</div>

An applied version of a Python project template. The contents of this project will be converted into a template by [Copier](https://copier.readthedocs.io/) and published in the [python-anything](https://github.com/ulgens/python-anything) repository.

## Required tools
- [prek](https://prek.j178.dev/installation/)

## Implemented Methods & Patterns
* **Linting & Formatting**: [Ruff](https://github.com/astral-sh/ruff) for linting and formatting, configured in `ruff.toml`.
* **Git Hooks**: [prek](https://prek.j178.dev/) runs pre-commit hooks defined in `.pre-commit-config.yaml`, including:
  * General checks (large files, merge conflicts, trailing whitespace, etc.)
  * `pyproject-fmt` for `pyproject.toml` formatting
  * `uv-lock` to keep the lockfile in sync
  * `ruff` for linting and formatting
  * `yamlfmt` for YAML formatting
  * `check-jsonschema` for GitHub Actions workflow validation
  * `zizmor` for GitHub Actions security auditing
  * `codespell` for spell checking
* **CI**: GitHub Actions workflows for running tests (`pytest`) and git hooks.
* **Dependency Management**: [uv](https://github.com/astral-sh/uv) with pinned versions in `pyproject.toml` and `uv.lock`.
* **Dependency Updates**: [Renovate](https://github.com/renovatebot/renovate) for automated dependency update PRs.
* **Testing**: [pytest](https://github.com/pytest-dev/pytest) with [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) for parallel test execution.

## Related Projects
- Use [ulgens/django-blasphemy](https://github.com/ulgens/django-blasphemy) for Django projects.

## Contribution
- Install git hooks by `prek install` and ensure your changes pass the checks before creating a pull request.
  - After `prek install`, git hooks will be automatically run while committing. To manually run the checks, use `prek run`.
