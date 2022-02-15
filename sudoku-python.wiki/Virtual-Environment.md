To specify the versions of the packages used, we set up a virtual environment for the project. This allows the project
to be replicated without any dependency conflicts.

### Setup

| Command | Description |
| --------|-------------|
|`pip3 install -U virtualenv`| Install virtualenv |
|`python3 -m virtualenv venv`| Install virtualenv |
|`virtual venv`              | Initialises a virtual environment (creates folder called venv)|
|`source venv/bin/activate`  | Start the virtual environment|
|`pip3 install -U -r requirements.txt`| From requirements.txt, installs all relevant dependencies to run program|
|`pip list` |Shows all packages installed in the environment|
|`deactivate` | Takes you out of the virtual environment and into the global environment|

### Set Version of Python

Command:

```bash
virtualenv --python=<path to python 3.9> <path/to/virtualenv/>
```

To check versions being used:

```bash
python3 --version
env/bin/python --version
```

#### IDE should be set with correct venv

Must ensure that the IDE is set with the appropriate venv, otherwise 
false positives may occur where the IDE cannot run correctly - but 
running `make` in the command line does. 

Check the IDE venv by looking at the `python interpreter`.