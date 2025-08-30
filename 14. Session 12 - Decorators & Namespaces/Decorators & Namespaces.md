# Decorators & Namespaces

## Namespaces
A namespace is a space that holds names(identifiers). Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values).

Example:
```
a = 4
b = 3

namespace syntax: {a: 4, b: 3}
```

There are 4 types of namespaces:

1. Built-In Namespace
2. Global Namespace
3. Enclosing Namespace
4. Local Namespace

### Scope and LEGB Rule
A scope is a textual region of a Python program where a namespace is directly accessible.

The interpreter searches for a name from the inside out looking in the local, enclosing, global, and finally the built-in scope. If the interpreter doesn't find the name in any of those locations, then Python raises a NameError exception.

### LEGB Rule
1. Built-In Namespace
2. Global Namespace
3. Enclosing Namespace
4. Local Namespace


## Decorators

A decorator in python is a function that receives another function as input and adds some functionality(decoration) to and it and returns it.

This can happen only because python functions are 1st class citizens.

There are 2 types of decorators available in python

- Built in decorators like `@staticmethod`, `@classmethod`, `@abstractmethod` and `@property` etc.
- User defined decorators that we programmers can create according to our needs.