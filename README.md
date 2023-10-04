# flake8-qt-tr

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ostr00000/flake8-qt-tr/main.svg)](https://results.pre-commit.ci/latest/github/ostr00000/flake8-qt-tr/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Flake8 extension for detecting incorrect QT translations.

## Installation

with `pip`:

```shell
pip install flake8-qt-tr
```

with [`pre-commit`](https://pre-commit.com/) ([doc](https://flake8.pycqa.org/en/latest/user/using-hooks.html)):

```yaml
repos:
  - repo: https://github.com/PyCQA/flake8
    rev: '' # pick a git hash/tag
    hooks:
      - id: flake8
        additional_dependencies:
          # ...
          - flake8-qt-tr
```

## Error Codes

| Code  | Description                                  | Example                            |
|-------|----------------------------------------------|------------------------------------|
| TR011 | Translation is formatted by f-string.        | `self.tr(f"Value: {val}")`         |
| TR012 | Translation is formatted by `format` method. | `self.tr("Value: {}".format(val))` |
| TR013 | Translation is formatted by printf-style.    | `self.tr("Value: %s" % val)`       |
