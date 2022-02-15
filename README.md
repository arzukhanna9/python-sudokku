# PYTHON SUDOKU

This program solves any problem to the [Sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku).

See [GitHub Wiki](https://github.com/arzukhanna/sudoku-python/wiki).

## Input

A text or JSON file with a grid representing the sudoku puzzle to be solved.

### Grid

A valid grid is one that:

* Contains a total of 81 integers in a 9x9 grid format
* Integers represent a cell and must be in range `0` to `9`
    * `0` - represents an empty cell that needs to be solved
    * `1` to `9` - are cells that have been solved and must not change
* Each row of the grid starts on a new line
* There are no duplicate integers in any row, column or 3x3 cell

#### Example Easy Puzzle

Source (text): [data/easy.txt](data/easy.txt)

```text
0 2 0 3 5 0 0 8 4
0 0 0 4 6 0 0 5 7
0 0 0 2 0 7 0 1 0
0 0 5 0 4 0 8 0 2
0 6 9 0 2 8 0 0 0
0 0 8 0 0 0 1 0 6
7 3 0 8 0 5 4 2 0
9 0 0 7 3 0 0 6 1
0 5 0 0 9 2 0 0 8
```

Source (json): [data/easy.json](data/easy.json)

```json
{
  "puzzle":
    [[0, 2, 0, 3, 5, 0, 0, 8, 4],
    [0, 0, 0, 4, 6, 0, 0, 5, 7],
    [0, 0, 0, 2, 0, 7, 0, 1, 0],
    [0, 0, 5, 0, 4, 0, 8, 0, 2],
    [0, 6, 9, 0, 2, 8, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 1, 0, 6],
    [7, 3, 0, 8, 0, 5, 4, 2, 0],
    [9, 0, 0, 7, 3, 0, 0, 6, 1],
    [0, 5, 0, 0, 9, 2, 0, 0, 8]]
}
```

## Output

Solved sudoku puzzles with same dimensions as input with all `0`'s replaced with integers in 
range from `1` to `9`. 

NOTE: Output solution and format is the same for both text and json input files.

#### Example Solved Puzzle

```bash
python3 solve_sudoku.py data/easy.txt

[[6 2 7 3 5 1 9 8 4]
 [8 1 3 4 6 9 2 5 7]
 [5 9 4 2 8 7 6 1 3]
 [1 7 5 9 4 6 8 3 2]
 [3 6 9 1 2 8 7 4 5]
 [2 4 8 5 7 3 1 9 6]
 [7 3 6 8 1 5 4 2 9]
 [9 8 2 7 3 4 5 6 1]
 [4 5 1 6 9 2 3 7 8]]
 ```

#### Example output when wrong file type given

Source: [data/invalid_file](data/invalid_file)

A log error is returned in the format below.

```bash
    $ python3 solve_sudoku.py data/invalid_file
    
    2021-07-16 09:10:16,535:ERROR:Cannot read file type None
```

## Virtual Environment

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

### Set Updated Version of Python

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

## Makefile

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

## Unit Testing

Known values are tested to known responses.The unit tests have been designed in a 
way to test the functionality of each small component of the program. Specifically, 
they test how the program handles both incorrect and correct inputs. Specific lists 
have been created to be tested by the test functions which all begin with `test_`.

Examples:
```python
GOOD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_WITH_DUPLICATES = [6, 5, 4, 1, 9, 8, 3, 7, 6]

def test_grid_list_valid():
    """Rows and columns valid"""
    assert sudoku.is_row_valid(GOOD_LIST)
    assert sudoku.is_column_valid(GOOD_LIST)


def test_grid_list_duplicates_invalid():
    """Row/Column has duplicates - invalid"""
    assert not sudoku.no_duplicates(LIST_WITH_DUPLICATES)
    assert not sudoku.no_duplicates(LIST_WITH_DUPLICATES)
```

### Hypothesis Testing 

A type of property-based testing that verifies the program code using a large 
range of relevant inputs. To use this, a list of valid and invalid inputs need to 
be declared and stored in a variable from which the hypothesis tests generate a 
random sample to test correctness of code.

#### `@given`
A decorator that takes a test function and turns it into a parametrized one which, 
when called, runs the test over a wide range data matching the specified data type.
* `sets` ensures that only one of each value in the specified range is used to 
generate the random test.
  
* `sampled_from` specifies the list from which the values are randomly being chosen 
from (initialised beforehand).


Example:
```python
VALID_SUDOKU_VALUES = list(range(1, 10))

@given(sets(sampled_from(VALID_SUDOKU_VALUES), min_size=9, max_size=9))
def test_has_correct_cells(row):
    "Row has no letters or incorrect integers"
    assert sudoku.no_letters(row) and sudoku.no_wrong_integers(row)
```

## Logging

The process of collecting information about events that occur in the operating system.
software of in communication. 

In enterprises, logging is used to:

1. Monitor behaviour (and apply automatic responses on some activity)
2. Help diagnose problems in an environment
3. Trace activity (E.g., transactions across many services)

### Logging Levels 

Levels are used for identifying the severity of an event. There are six logging levels:
1. CRITICAL
2. ERROR
3. WARNING
4. INFO
5. DEBUG
6. NOTSET

INFO level is often set as the default level. This program predominantly uses the 
debug level.

### Properties used:

Source: [log.properties](log.properties)

`[logger_root]`

  * `level = INFO` (default level is INFO)
  * `handlers = console,file` (logs handled in both file and console)

`[handler_file]`
  * `class = logging.handlers.RotatingFileHandler(filename, mode = 'a', maxBytes, 
    backupCount)`
  * Allows the file to rollover at a predetermined size. When size (maxBytes) is about 
    to be exceeded, file is closed and new file is silently opened for output.
  * backupCount must be at least 1 for rollover to occur.

`[handler_console]`
  * `class = StreamHandler(sys.stdout,)`
  * Sends logging output to sys.stdout

`[formatter_default]`
  * `format=%(asctime)s:%(levelname)s:%(message)s`
  * Specifies format of output. Used for both file and console handling.

### Set-up in Main Program

```python 
logging.config.fileConfig(
  fname="log.properties", defaults={"logfilename": "sudoku.log"})

logger = logging.getLogger()

if verbose:
    logger.setLevel(logging.DEBUG)
```

### Set-up in Lib Program

```python 
log = logging.getLogger()
```

## Pipelines

### GitLab Pipelines

A pipeline is declared using a YAML file, [.gitlab-ci.yml](public/.gitlab-ci.yml).

A pipeline is comprised of:

* Jobs: Define what and how to run.
* Stages: Define when to run the jobs.

To configuring a pipeline:

* Add a YAML file called [.gitlab-ci.yml](public/.gitlab-ci.yml) to the project.
* The YAML file will dictate the structure, and order of execution of the pipeline.
* When a `push` is made to the `origin` and GitLab finds a `.gitlab-ci.yml` file inside the repository root a Pipeline
  starts building automatically.

### Job Keywords used

| Keyword | Description |
| --------|-------------|
| [before_script](https://docs.gitlab.com/ee/ci/yaml/#before_script) | Override a set of commands that are executed before job |
| [cache](https://docs.gitlab.com/ee/ci/yaml/#cache) | List of files that should be cached between subsequent runs |
| [image](https://docs.gitlab.com/ee/ci/yaml/#image) | Use Docker images |
| [stage](https://docs.gitlab.com/ee/ci/yaml/#stage) | Defines a job stage (E.g., build) |
| [variables](https://docs.gitlab.com/ee/ci/yaml/#variables) | Define job variables on a job level |

## GitHub 

### Set-up remote 

* Rename current Gitlab remote
  ```bash
  $ git remote rename origin gitlab
  ```

* Update Git to add new remote to GitHub: 
  ```bash
  $ git remote add github git@github.com:arzukhanna/sudoku-python.git
  ```

* Force push main branch from GitLab to GitHub
  ```bash
  $ git checkout main
  $ git push -fu github main
  ```
  
* Push develop and feature branch from GitLab to GitHub
  ```bash
  $ git checkout develop
  $ git push -u github develop
  $ git checkout feature
  $ git push -u github feature
  ```

* In GitHub, protect develop and main branches. These are long-lived and 
  should be "protected". ( Settings > Branches)

### Pipelines

A pipeline is declared using a YAML file, [.python.yml](.github/workflows/python.yml) 
which is stored in a new directory [.github/workflows/](.github/workflows).

#### Workflow Commands 

| Syntax | Description |
| --------|-------------|
| name | Name of the workflow which appears in Actions tab of the GitHub repository. |
| on: [push] | Job runs every time a change is pushed. |
| jobs | Groups together all jobs to be run in workflow file. |
| runs-on: ubuntu-latest | Configures the job to run on an Ubuntu Linux runner (The job will execute on a fresh virtual machine hosted by GitHub.|
| steps |  Groups together all steps. Each nested item is a separate action / shell command.|
| cache | Manually caches workflow files. |
| `if: github.ref == 'refs/heads/main` | Will only run if on main branch. | 


## Docker Images

### Writing Dockerfile

Source: [Dockerfile](Dockerfile)

* `FROM` specifies the base image on which the docker image will be built.
* `COPY` add files from the Docker client’s current directory.
* `RUN` specifies the additional commands to execute.
* `ENTRYPOINT` sets parameters that will execute (these) cannot be overwritten 
  from the command line. 
* `CMD` sets default commands and/or parameters, which can be overwritten from 
  the command line when docker container runs.
  
### Registry vs Image 

* A registry is a storage and content delivery system, holding named Docker images, available in different 
  tagged versions. Users interact with a registry by using docker push and pull commands.

### Building Image Locally

1. Build dockerfile and start executing the commands.

```bash
docker build --tag python-sudoku .
```

2. Run the dockerfile.

```bash
docker run python-sudoku ./solve_sudoku.py <data file>
```

### Pushing Image to Docker Hub

```bash
docker tag python-sudoku arzukhanna/python-sudoku
docker push arzukhanna/python-sudoku
```

### Pulling Image from Docker Hub

```bash
docker pull arzukhanna/python-sudoku
docker run arzukhanna/python-sudoku:latest ./solve_sudoku.py <data file>
```

### Docker Image onto Container Registry in GitLab 

```python
build:
  image: docker:20.10.7
  stage: build
  services:
    - docker:dind
  before_script:
    - |
      echo ${CI_BUILD_TOKEN} | \
        docker login \
          --username ${CI_REGISTRY_USER} \
          --password-stdin \
          ${CI_REGISTRY}
  script:
    - |
      docker build \
        --pull \
        --tag ${CI_REGISTRY_IMAGE} \
        --tag ${CI_COMMIT_SHORT_SHA} \
        .
    - docker push ${CI_REGISTRY_IMAGE}

production:
  stage: production
  image:
    name: ${CI_REGISTRY_IMAGE}:latest
    entrypoint: [""]
  script:
    - echo Running image "${CI_REGISTRY_IMAGE}" ...
    - ./solve_sudoku.py --version
    - ./solve_sudoku.py -h
    - echo CI_PROJECT_DIR "${CI_PROJECT_DIR}"
    - echo CI_BUILDS_DIR "${CI_BUILDS_DIR}"
    - echo CI_PROJECT_PATH "${CI_PROJECT_PATH}"
    - ./solve_sudoku.py ${CI_PROJECT_DIR}/data/easy.json
```

### Testing Docker image from another GitLab repository

```python
image: docker:latest

services:
  - docker:dind

variables: 
    REGISTRY: registry.gitlab.com/themarlogroup/training/students/akhanna/python-sudoku
    IMAGE: arzukhanna/python-sudoku:latest

before_script:
  - |
    echo ${CI_BUILD_TOKEN} | \
      docker login \
      --username ${CI_REGISTRY_USER} \
      --password-stdin \
      ${REGISTRY}

test:
  stage: test
  script:
    - docker run 
        -v "${CI_PROJECT_DIR}":/mnt/
        ${IMAGE} /mnt/hard_puzzle.json
```

* `docker run -v "${CI_PROJECT_DIR}":/mnt/ ${IMAGE} /mnt/hard_puzzle.json`
  * Creates a volume from the local project directory and mounts point inside container
  

* `mnt` (`mount`) mounts a file or directory on the host machine into a container.
The file/directory is referenced by its path on the host machine. When volume (`-v`) is 
used, a new directory is created within Docker’s storage directory on the host machine, 
and Docker manages that directory’s contents.

### Other Commands

* Removing container: `docker rm <container name>`
* Remove images: `docker rmi <image name>`


## Requirements

* [Package Versions Required](requirements.txt)

## References

* [Sudoku Code](https://www.youtube.com/watch?v=G_UYXzGuqvM)
* [How to create a Virtual Environment](https://www.youtube.com/watch?v=N5vscPTWKOk)
* [Make Guidelines](https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make)
* [GitLab Pipelines](https://docs.gitlab.com/ee/ci/yaml/)
* [Python Logging](https://zetcode.com/python/logging/)
* [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
* [Working with GIT remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
* [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions)
* [Migrating from GitLab CI/CD to GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/migrating-from-gitlab-cicd-to-github-actions)
* [CMD vs Entrypoint](https://phoenixnap.com/kb/docker-cmd-vs-entrypoint)
