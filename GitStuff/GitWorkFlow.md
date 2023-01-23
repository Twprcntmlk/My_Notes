# Git Work Flow

## Step 1: Create Issue
- On the Repo, click the Issues Tab
- Create New Issue
- Title & Comment
- Submit New Issue and <b>Note the Issue #</b>

## Step 1A: Possible Additions
```bash
# possible stuff
mkdir ~/file
cd ~/file
git clone {rep0 link here}
```
## Step 2: Create Local Branch
```bash
git checkout -b {username}/{task-name}
```
## Step 3: Work Complete!
- Work Complete?

## Step 4: Add/Commit/Push
```bash
git add {file-name} or git add .

EDITOR='code -- wait' git commit

1 -- Pull request title
2 -- {verb} - {subject}
3 -- {Auto Close Keyword } {Issue Number}

```

#### Auto Close Keywords
- close
- closes
- closed
- fix
- fixes
- fixed
- resolve
- resolves
- resolved

```bash
git push origin
# probably need to get new origin branch
# note link to the PR (Pull Request)
```

## Fetching changes to main and FF your local copy
```bash
git fetch --all --prune
git checkout main
git merge --ff-only
```
## Clean up Local Branch
```bash
git branch --delete --force {username}/{task-name}
```


## commands to note
```bash
git restore --staged <file>
git ammend
```

## Clean up redundant PR
- Obsoleted by {Pull Request Number}




- set upstream
git branch --set-upstream-to main

- create topic branch
git checkout main -b my-branch-name

- git push origin
