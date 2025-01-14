# package

This repository is a template for the [cradle](https://github.com/cvxgrp/cradle)
system.

The package template is most useful when the final
goal is the release of software to a registry, e.g. pypi.
It features include

* uv support
* curated set of pre-commit hooks
* DevContainer
* Makefile
* github ci/cd workflows
* marimo support
* JupyterBook
* pdoc documentation

```bash
    create  uv.lock
    create  .pre-commit-config.yaml
    create  README.md
    create  .devcontainer
    create  .devcontainer/startup.sh
    create  .devcontainer/devcontainer.json
    create  Makefile
    create  .gitignore
    create  LICENSE.txt
    create  .github
    create  .github/CONTRIBUTING.md
    create  .github/workflows
    create  .github/workflows/release.yml
    create  .github/workflows/pre-commit.yml
    create  .github/workflows/book.yml
    create  .github/workflows/ci.yml
    create  .github/CODE_OF_CONDUCT.md
    create  .github/dependabot.yml
    create  book
    create  book/docs
    create  book/docs/api.md
    create  book/docs/reports.md
    create  book/docs/index.md
    create  book/docs/marimo.md
    create  book/_config.yml
    create  book/_toc.yml
    create  book/marimo
    create  book/marimo/demo.py
    create  pyproject.toml
    create  .env
    create  src
    create  src/tests
    create  src/tests/conftest.py
    create  src/tests/test_trivial.py
    create  src/tests/resources
    create  src/tests/resources/.gitkeep
    create  src/tests/__init__.py
    create  src/{{ project_name }}
    create  src/{{ project_name }}/add.py
    create  src/{{ project_name }}/__init__.py
```
