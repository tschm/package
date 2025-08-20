# 📦 package --- qCradle template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/tschm/package/badge)](https://www.codefactor.io/repository/github/tschm/package)
[![Created for qCradle](https://img.shields.io/badge/Created%20for-qCradle-blue?style=flat-square)](https://github.com/cvxgrp/cradle)

The package template is most useful when the final
goal is the release of software to a registry, e.g. pypi.
It features include

* 🚀 Uses uv for dependency management and hatch for build management
* ✅ Offers a list of curated pre-commit hooks
* 🔄 GitHub Actions for continuous integration
* 🧪 Automated testing with pytest
* 🧹 Code formatting with ruff
* 📊 Interactive notebooks with marimo
* 📚 Documentation generation with pdoc

## 🚀 Getting Started

Using the template is easy. 
Use the qcradle command to create a new project:

```bash
uvx qcradle
```

This command:
- Installs qcradle if not already installed
- Creates a new project using the template
- Installs the project dependencies

### **📝 Project Setup**

1. Update project information in `pyproject.toml`:
   - Project name, description
   - Author information and email addresses

2. Configure GitHub repository settings:
   - Enable GitHub Pages (from GitHub action)
   - Set up trusted publishing for PyPI releases

3. Install pre-commit hooks:
   
   ```bash
   make check
   ```

## 🛠️ Development

### **Common Commands**

```bash
# Run tests
make test

# Check code quality
make check

# Clean project
make clean

# Build documentation
make book

# Start Marimo notebooks
task docs:marimo
```

## 📚 Documentation

The project includes Marimo notebooks for interactive documentation:

```bash
# Start Marimo server
task docs:marimo
```

Documentation is automatically built and published to GitHub Pages on push.

## 👥 Contributing

* 🍴 Fork the repository
* 🌿 Create your feature branch (git checkout -b feature/amazing-feature)
* 💾 Commit your changes (git commit -m 'Add some amazing feature')
* 🚢 Push to the branch (git push origin feature/amazing-feature)
* 🔍 Open a Pull Request


## 🔍 Project Structure

```
├── .github/            # GitHub Actions workflows and configurations
├── book/               # Documentation and notebooks
│   └── marimo/         # Marimo interactive notebooks
├── src/                # Source code
│   └── project_name/   # Main package code
├── tests/              # Test suite
├── Makefile            # Simple command shortcuts
├── Taskfile.yml        # Task automation definitions
├── pyproject.toml      # Python project configuration
└── README.md           # This file
```

## ⚠️ PyPI Publishing Note

When first setting up the project, you'll need to register it on 
PyPI before the automated publishing workflow will succeed. 
The GitHub Actions workflow is configured to publish from 
the 'release' environment.

## 📬 Contact

Thomas Schmelzer - [@tschm](https://github.com/tschm)

🔗 Project Link: <https://github.com/tschm/package>
