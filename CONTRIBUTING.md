# Contributing to python-anything-applied

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Getting Started

### Prerequisites
- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- [prek](https://prek.j178.dev/installation/) for git hooks

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ulgens/python-anything-applied.git
   cd python-anything-applied
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Install git hooks**
   ```bash
   prek install
   ```

## Development Workflow

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add type hints to all functions
   - Follow PEP 8 style guidelines
   - Add docstrings following PEP 257

3. **Run tests**
   ```bash
   cd src
   uv run pytest -n auto
   ```

4. **Run linters**
   ```bash
   prek run
   ```

### Code Quality Standards

- **Type Hints**: All functions must have type annotations
- **Docstrings**: All public functions/classes must have docstrings
- **Tests**: New features should include tests
- **Linting**: All code must pass ruff checks
- **Formatting**: Code must be formatted with ruff

### Git Commit Messages

Follow conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

Example:
```
feat: add user authentication module

- Implement JWT-based authentication
- Add login and logout endpoints
- Include tests for auth flows
```

### Pre-commit Hooks

Git hooks will automatically run when you commit:
- Code formatting (ruff)
- Linting (ruff)
- YAML/TOML validation
- Trailing whitespace removal
- Large file detection
- Private key detection

To manually run all hooks:
```bash
prek run --all-files
```

## Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass** locally before submitting
4. **Update the README** if needed
5. **Submit your PR** with a clear description of changes

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
Describe how you tested your changes

## Checklist
- [ ] Tests pass locally
- [ ] Code is formatted and linted
- [ ] Documentation updated
- [ ] Git hooks pass
```

## Questions or Issues?

- Open an issue for bugs or feature requests
- Check existing issues before creating new ones
- Provide detailed reproduction steps for bugs

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community

Thank you for contributing! 🎉
