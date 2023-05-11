## Cmd.cmdloop(intro=None) 


* An interpreter instance will recognize a command name `foo` if and only if it has a method `do_foo()`.
* A line beginning with the character `'?'` is dispatched to the method `do_help()`. 
* As another special case, a line beginning with the character `'!'` is dispatched to the method `do_shell()` (if such a method is defined).
* All subclasses of Cmd inherit a predefined `do_help()`. 
This method, called with an argument 'bar', invokes the corresponding method `help_bar()`, and if that is not present, prints the docstring of `do_bar()`, if available.
