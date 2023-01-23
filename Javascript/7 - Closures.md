### Overview: Children have Access to parent scope

## Closure
- A function along with a saved reference to the 'lexical environment'
  it was defined in. Simply put, this means functions have access
  to all of the variables in scope at the time of definition, even if the parent
  function has returned.

## Lexical Environment
- An internal data structure used for keeping track of identifiers (variable and
  function names) and their values. A lexical environment stores all of the
  locally available identifiers as well as a reference to the parent environment.

## Lexical Scoping
- The scoping system in JavaScript that ensures all code blocks have access
  to all identifiers in their parent environment. When an identifier is not defined
  locally, JavaScript will look to the parent environment for it. If it is still not
  found there, it will look in grandparent's environment and so on before looking in
  the global environment.
