A GitHub Pipeline is declared using a YAML file, [.python.yml](https://github.com/arzukhanna/sudoku-python/tree/4-duplicate-project-on-github/.github/workflows) 
which is stored in directory, [.github/workflows/](https://github.com/arzukhanna/sudoku-python/tree/4-duplicate-project-on-github/.github/workflows).

### Workflow Commands 

| Syntax | Description |
| --------|-------------|
| name | Name of the workflow which appears in Actions tab of the GitHub repository. |
| on: [push] | Job runs every time a change is pushed. |
| jobs | Groups together all jobs to be run in workflow file. |
| runs-on: ubuntu-latest | Configures the job to run on an Ubuntu Linux runner (The job will execute on a fresh virtual machine hosted by GitHub.|
| steps |  Groups together all steps. Each nested item is a separate action / shell command.|
| cache | Manually caches workflow files. |
| `if: github.ref == 'refs/heads/main` | Will only run if on main branch. | 
