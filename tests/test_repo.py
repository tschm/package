from pathlib import Path
import os

import pytest
from copier import run_copy


@pytest.fixture()
def repo(tmp_path):
    # Assuming `run_copy` is copying a folder to `tmp_path`
    run_copy(".", tmp_path, data={"project_name": "maffay"})

    # Collect all files in the directory and return as a set of relative paths
    # Use relative_to to get the file paths relative to `tmp_path`
    return set(
        [file.relative_to(tmp_path) for file in tmp_path.rglob("*") if file.is_file()]
    )


def test_repo(repo):
    assert Path(".pre-commit-config.yaml") in repo
    assert Path("Makefile") in repo
    assert Path(".gitignore") in repo
    assert Path("README.md") in repo
    assert Path(".github/workflows/pre-commit.yml") in repo
    assert Path(".github/workflows/book.yml") in repo
    assert Path(".devcontainer/devcontainer.json") in repo
    assert Path(".devcontainer/startup.sh") in repo
    assert Path(".github/dependabot.yml") in repo
    assert Path("uv.lock") in repo

def test_make_install():
    os.system("make install")

def test_make_test():
    os.system("make test")

def test_make_help():
    os.system("make help")
