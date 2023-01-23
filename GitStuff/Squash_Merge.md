It can be tiresome to rebase feature branches with many commits. You may have several commits that conflict with your main branch. Before rebasing such branches, you may want to squash your commits together, and then rebase that single commit, so you can handle all conflicts at once. Here’s how to do that.

Imagine you’ve been working on the feature branch show_birthday, and you want to squash and rebase it onto main.

First, switch to the feature branch:
```
$ git switch show_birthday
```
Second, use rebase to squash the branch on top of its original base commit:
```
$ git rebase --keep-base -i main
```
What do those two flags do?

--keep-base flag tells Git to rebase on to the base commit from main that the branch was created from. This is different to the default behaviour of using the latest commit in main.

-i is short for --interactive, which enables rebase’s interactive mode. This will open your text editor with a file you can use to select rebase operations.

Third, change the rebase file to squash all commits into the first one with “fixup”. When the file opens, you’ll see contents like this:
```
pick e81a5f1 start on showing birthday
pick 72c9e48 database migration
pick 65cb164 template change

# Rebase fc63cec..65cb164 onto fc63cec (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amendingx
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
...
(Further comments removed for brevity.)
```
The first lines show the commits on your current branch, and the rebase operations to perform with them. The remaining lines are comments with a mini cheatsheet of the possible operations.

To tell rebase to squash all commits into the first one, change all commit lines but the first one to start with “f”:
```
pick e81a5f1 start on showing birthday
f 72c9e48 database migration
f 65cb164 template change

# Rebase fc63cec..65cb164 onto fc63cec (3 commands)
#
# Commands:
...
```
(You can also write “fixup” in full, but it’s not worth the typing.)
Note that there’s also the “s” / “squash” command, which allows you to combine edit the squashed commit message. Generally I prefer using “f” / “fixup”, and then fixing the first commit’s message if necessary with “r” / “reword”.

Fourth, save and close the file, and Git will perform the rebase, squashing all commits into one. After this completes, you can look at the git log to see your single commit.

Fifth, you can now rebase your single commit onto your main branch. You may want to first pull the latest version of your main branch:
```
$ git fetch --all --prune
$ git switch main
$ git merge --ff-only
$ git switch show_birthday
```
Then, rebase your feature branch:
```
$ git rebase -i main
```
It’s not really necessary to use -i for interactive mode here, since you don’t need to make any changes. But I would encourage you to make a habit of using interactive mode, to double check what you’re rebasing.

As Git applies the rebase, you might have to deal with conflicts, and complete the commit git rebase --continue. This is easier than before squashing though, as now all the branch changes are in a single commit.

And, ta-daa, you’ve done it. You’ve squashed and rebased your branch!

Source: https://adamj.eu/tech/2022/03/25/how-to-squash-and-rebase-a-git-branch/
