1. EOF - In computing, end-of-file (EOF) is a condition in a computer operating system where no more data can be read from a data source. The data source is usually called a file or stream.


2. MY_ROOT="$( cd "$( dirname "${0}" )" && pwd )"

- ${} - acts as a kind of quoting for variables.
- $() - acts as a kind of quoting for commands but they're run in their own context.
- dirname - gives you the path portion of the provided argument.
- pwd - gives the current path.
- && - is a logical and but is used in this instance for its side effect of running commands one after another.

3. fi closes the if
