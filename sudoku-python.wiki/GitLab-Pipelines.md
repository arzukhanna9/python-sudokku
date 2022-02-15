A pipeline is declared using a YAML file, [.gitlab-ci.yml](https://github.com/arzukhanna/sudoku-python/blob/4-duplicate-project-on-github/.gitlab-ci.yml).

A pipeline is comprised of:

* Jobs: Define what and how to run.
* Stages: Define when to run the jobs.

To configuring a pipeline:

* Add a YAML file called [.gitlab-ci.yml](https://github.com/arzukhanna/sudoku-python/blob/4-duplicate-project-on-github/.gitlab-ci.yml) to the project.
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