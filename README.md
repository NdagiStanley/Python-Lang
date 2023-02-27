# Python

Python programming Language

## Installation

```bash
brew install python
```

### Versions

Recommended: [pyenv](https://github.com/pyenv/pyenv)

Have (the `PYENV` portion of my [.zshrc](https://github.com/NdagiStanley/dotfiles/blob/main/.zshrc)):

```sh
...
## PYENV
export PYENV_ROOT="$HOME/.pyenv"
...
```

in your `.zshrc` or `.bashrc` (or equivalent) then install `pyenv`:

```bash
brew install pyenv
```

Common commands:

```bash
pyenv install -l
pyenv install 3.11
pyenv global 3.11
```

Further: running `pyenv local 3.11` creates a `.python-version` file specifying the default python version when you _cd_ into the directory.

### Virtual environment

Recommended: [pipenv](https://pipenv.pypa.io/en/latest/)

Other: virtualenv, virtualenvwrapper

Install `pipenv`:

```bash
brew install pipenv
```

Common commands:

```bash
pipenv run python3 main.py
pipenv shell
```

## Implementation

Run:

```bash
python3 main.py
```

## More

- [Design patterns][dp]
- [SOLID][solid]

[dp]: /Design_patterns
[solid]: /SOLID

---
Ref:
- https://devguide.python.org/internals/exploring/
- https://realpython.com/products/cpython-internals-book/
