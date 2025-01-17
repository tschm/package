# package

[![PyPI version](https://badge.fury.io/py/{{ project_name }}.svg)](https://badge.fury.io/py/{{ project_name }})
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![CI](https://github.com/tschm/package/actions/workflows/ci.yml/badge.svg)](https://github.com/tschm/package/actions/workflows/ci.yml)
[![Created for Cradle](https://img.shields.io/badge/Created%20for-Cradle-blue?style=flat-square)](https://github.com/cvxgrp/cradle)

The package template is most useful when the final
goal is the release of software to a registry, e.g. pypi.
It features include

* Uses uv for dependency management and hatch for build management
* Offers a list of curated pre-commit hooks
* GitHub Actions for continuous integration
* Automated testing with pytest
* Code formatting with ruff
* Interactive notebooks with marimo
* Documentation generation with pdoc
* Support of a DevContainer

## Development Commands

```bash
make fmt     # Install pre-commit hooks and run them on all files
```

## Contributing

* Fork the repository
* Create your feature branch (git checkout -b feature/amazing-feature)
* Commit your changes (git commit -m 'Add some amazing feature')
* Push to the branch (git push origin feature/amazing-feature)
* Open a Pull Request

## Contact

Thomas Schmelzer - [@tschm](https://github.com/tschm)

Project Link: <https://github.com/tschm/package>
