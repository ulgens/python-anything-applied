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

## Required tools
- [prek](https://prek.j178.dev/installation/)

## Implemented Methods & Patterns
* ruff: ruff checks are run as git hooks and wrapped in CI. Configuration is in `ruff.toml`.

## Contribution
- Install git hooks by `prek install` and ensure your changes pass the checks before creating a pull request.
  - After `prek install`, git hooks will be automatically run while committing. To manually run the checks, use `prek run`.
