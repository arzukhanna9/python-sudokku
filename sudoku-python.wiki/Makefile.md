Makefiles are special format files that help build and manage projects automatically through use of `make`. The makefile
used specifies the virtual environment set-up process which can be accessed using `make help`. The tools below are
automatically run when the `make` command is run.

Source: [Make Guidelines](https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make)
Makefile: [Makefile](Makefile)

### Make Components

| Tool | Description |
| --------|-------------|
| [isort](https://pycqa.github.io/isort/) | Sorts Inputs |
| [black](https://pypi.org/project/black/) | Format the Code |
| [flake8](https://pypi.org/project/flake8/) | Style Checks |
| [pylint](https://pypi.org/project/pylint/) | Static Code Checks |
| [pytest](https://pypi.org/project/pylint/) | Unit Testing Framework |