## Set-up remote 

1. Rename current Gitlab remote
  ```bash
  $ git remote rename origin gitlab
  ```

2. Update Git to add new remote to GitHub: 
  ```bash
  $ git remote add github git@github.com:arzukhanna/sudoku-python.git
  ```

3. Force push main branch from GitLab to GitHub
  ```bash
  $ git checkout main
  $ git push -fu github main
  ```
  
4. Push develop and feature branch from GitLab to GitHub
  ```bash
  $ git checkout develop
  $ git push -u github develop
  $ git checkout feature
  $ git push -u github feature
  ```

5. In GitHub, protect develop and main branches. These are long-lived and should be "protected". ( Settings > Branches)
6. Make develop branch the 'default' branch.

