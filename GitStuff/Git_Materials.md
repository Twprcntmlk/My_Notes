
## 1. Create a local topic branch
Create a new branch from ``main``.
``` sh
[container]% git checkout -b yourusername/topic
[container]% git status

Your branch is up to date with 'main'.
nothing to commit, working tree clean
```

## 2. Make some changes and create a local commit
``` sh
[container]% code --add ~/mm
[container]% touch onboarded/<username>.md
[container]% code onboarded/<username>.md
# should add this folder to the sidebar of your VSCode workspace
```

### Stage the file.

``` sh
[container]% git add {file}
or
[container]% git add .

- Stages new and modified files only, NOT deleted files
git add --update
git add -u
```

### Make a new commit that includes your changes.
- https://cbea.ms/git-commit/
``` sh
[container]% git commit -m 'yourusername onboarding'

```
- For VSCode Editor Commits
``` sh
[container]% EDITOR='code --wait' git commit
# should open a new editor in VSCode and wait until that editor is closed
```
Note: If this is your preferred workflow, consider adding ``export EDITOR='code --wait'`` to your shell initialization (e.g., ``~/.profile``)


## 3. Push your local branch to GitHub and create a Pull Request

Now that you have a local branch with something interesting to share, push it to GitHub.

``` sh
[container]% git push origin
```

Open the URL provided in the commit message and [create a Pull Request (PR)](https://github.com/monetarymetals/onboarding-exercise/pulls) for review.

## 6. Request a review and merge your Pull Request into ``main``

- [Assign a reviewer](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review) who will approve your Pull Request.

- Once approved, use the Pull Request interface to [squash and merge](https://docs.github.com/en/github/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squash-and-merge-your-pull-request-commits) it.

- Once merged, verify that the issue you created in [step zero](#0-create-a-github-issue) was automatically closed.

- If it wasn’t, you’ll want to understand why before manually referencing your PR and closing it.



## 7. Fetch the upstream changes to ``main`` and fast-forward your local copy

Our workflow requires treating your local mainline branch (e.g., ``main``) as read-only.
It is fundamentally different from your topic branches in this respect.
Its only modifications should come from retrieving additional commits from GitHub.
Those commits should come from merged PRs.

Fetch the updates performed from merging the Pull Request back down from GitHub to your local repository.

``` sh
[container]% git fetch --all --prune
```

Now checkout ``main`` and fast forward it to include the newly-fetched changes.

``` sh
[container]% git checkout main

[container]% git merge --ff-only

```
## You can now delete your now-merged topic branch if you wish.

``` sh
[container]% git branch --delete --force yourusername/onboarding
```


Many people like to use ``git checkout main ; git pull`` for this step, but [git-pull](https://www.git-scm.com/docs/git-pull) performs quite a bit of magic that can be difficult to unwind.
Until you are comfortable knowing *precisely* what ``git pull`` will do in a given situation, the narrower and more explicit ``git fetch … ; git merge --ff-only …`` is likely the best approach.


# IMPORTANT

- This workflow implies that the *only* modifications ever made to one’s local clone of ``main`` is to fast-forward it after retrieving updates.
This is intentional.

- ``main`` should be treated as releasable at all times.
The responsibility to maintain it as such is shared among both the committer *and* the reviewer for each commit.
This further implies that every commit has a reviewer.



## Other Commands to Master
- ``git commit --ammend``

## Next steps

* If you’re new to Git or GitHub, consider watching [this tutorial](https://youtu.be/RGOj5yH7evk).
* [This video](https://youtu.be/lSnbOtw4izI) has some good tips on how to review a Pull Request.
  These are also great resources:
  * [Writing a Proper GitHub Issue](https://medium.com/nyc-planning-digital/writing-a-proper-github-issue-97427d62a20f)
  * [How to Write the Perfect Pull Request](https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/)
  * [How to Create a Good Pull Request — and How to Review One?](https://betterprogramming.pub/how-to-create-a-good-pull-request-and-how-to-review-one-c30a13f61fd2)
* [This write-up](https://blog.mozilla.org/webdev/2011/11/21/git-using-topic-branches-and-interactive-rebasing-effectively/) highlights some great techniques as well.
* GitHub hosts some [great docs](https://docs.github.com/en/github/collaborating-with-pull-requests), but ignore the portion on “forks”.
  That won’t apply to MM’s use of GitHub.
