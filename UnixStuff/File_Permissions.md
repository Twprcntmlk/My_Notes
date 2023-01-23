# File Permissions

## What are permissions?
On a UNIX web server, every single file and folder stored on the hard drive has a set of permissions associated with it, which says who is allowed to do what with the file. Every file (and folder) also has an “owner” and a “group” associated with it. If you created the file, then you are usually the owner of that file, and your group, or the group associated with the folder you created the file in, will usually be associated with that file.

Who can do stuff?
There are three types of people that can do stuff to files – the Owner of the file, anyone in the Group that the file belongs to, and Others (everyone else). In UNIX, these 3 types of people are referred to using the letters:
- U (for Owner, or User in UNIX-speak!),
- G (for Group)
- O (for Others).

## What stuff can you do?
There are three basic things that can be done to files or folders:

You can read the file. For folders, this means listing the contents of the folder.
You can write to (change) the file. For folders, this means creating and deleting files in the folder.
You can execute (run) the file, if it’s a program or script. For folders, this means accessing files in the folder.
What do all these funny letters and numbers mean?!
That’s the basics of permissions covered. As you can see, there’s not much to them really!

The confusion often occurs when you have to start actually setting permissions on your file server. CGI scripts will tell you to do things like “chmod 755” or “Check that the file is executable”. Also, when you use FTP or SSH, you’ll see lots of funny letters next to the files (such as rwxrw-rw-). We’ll now explain what all these hieroglyphics mean!

When you FTP to your web server, you’ll probably see something like this next to every file and folder:

###  Attributes list
This string of letters, drwxrwxrwx, represents the permissions that are set for this folder. (Note that these are often called attributes by FTP programs.) Let’s explain what each of these letters means:
| d         | r     | w     | x       | r     | w     | x       | r     | w     | x       |
|-----------|-------|-------|---------|-------|-------|---------|-------|-------|---------|
|           | Owner | Owner | Owner   | Group | Group |Group    | Other | Other | Other   |
| Directory | Read  | Write | Execute | Read  | Write | Execute | Read  | Write | Execute |

As you can see, the string of letters breaks down into 3 sections of 3 letters each, representing each of the types of users (the owner, members of the group, and everyone else). There is also a “d” attribute on the left, which tells us if this is a file or a directory (folder).

If any of these letters is replaced with a hyphen (-), it means that permission is not granted. For example:

drwxr-xr-x
A folder which has read, write and execute permissions for the owner, but only read and execute permissions for the group and for other users.
-rw-rw-rw-
A file that can be read and written by anyone, but not executed at all.
-rw-r--r--
A file that can be read and written by the user, but only read by the group and everyone else.
Using numbers instead of letters
As we said earlier, you’ll often be asked to do things using numbers, such as “set 755 permissions”. What do those numbers mean?

Well, each of the three numbers corresponds to each of the three sections of letters we referred to earlier. In other words, the first number determines the owner permissions, the second number determines the group permissions, and the third number determines the other permissions.

Each number can have one of eight values ranging from 0 to 7. Each value corresponds to a certain setting of the read, write and execute permissions, as explained in this table:

|Number|Read (R)|Write (W)|Execute (X)|
|------|--------|---------|-----------|
|  0   |  No    |  No     |   No      |
|  1   |  No    |  No     |   Yes     |
|  2   |  No    |  Yes    |   Yes     |
|  3   |  No    |  Yes    |   Yes     |
|  4   |  Yes   |  No     |   No      |
|  5   |  Yes   |  No     |   Yes     |
|  6   |  Yes   |  Yes    |   No      |
|  7   |  Yes   |  Yes    |   Yes     |

So, for example:

chmod 777 is the same as rwxrwxrwx

chmod 755 is the same as rwxr-xr-x

chmod 666 is the same as rw-rw-rw-

chmod 744 is the same as rwxr--r--

## Commands Examples
```bash
chmod -R -V a-wrx
chmod -R -V a+wrx
chmod -R -V ugo-wrx,ugo-wrx
chmod -R -V ugo+wrx,ugo+wrx
```
-R --recursive
-V --verbose


```bash
ls --all -l ~/file
ls -la
umask 022
trolling with umask 777
```
## Changing Owner Persmissions
```bash
sudo chown -R mm-dev:mm-dev ~./shh
# Note mm-dev and shh should be change depending user:group
```
## References
https://www.elated.com/understanding-permissions/
