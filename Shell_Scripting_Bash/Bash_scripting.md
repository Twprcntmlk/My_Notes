# Shells vs. Scripts

## Bash Shell
- BASH - Bourne Again Shell
### Difference Between Shells and Scripts
- Shell:
    - is a a program that interprets the commands I type in the terminal and passes them to operating system
- Script:
    - is a file containing command for shell

### Benefits of Bash Shell

### Benefits of Creating Scripts

### Bash Script Structure
- Starts with:
```bash
#! /bin/bash
echo "This is my first script"
exit 0
```

https://tldp.org/LDP/abs/html/exitcodes.html
exit code 1 = error
exit code 0 = pass

### Commenting
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html
```bash
# You add an comment like this
# Author: Full Name
# Date Created: Today's Date
# Last Modified: Date Modified
# Description: What Script Does
# Usage: How to run file
```

### Setting up Secure Script Permissions (744)
- https://chmod-calculator.com/
- ls -l

### Adding Script in PATH
- the PATH variable tells the shell where to search for executable files
- we can add folders to the path variable by modifying the .profile file
- and that makes the available system-wide

## Variables and Shell Expansions
