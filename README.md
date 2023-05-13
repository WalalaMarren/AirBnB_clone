DESCRIPTION OF PROJECT
This project is a commandline interpreter, a part of the AirBnB web application clone that can be used to manipulate the web application.

DESCRIPTION OF THE COMMAND INTERPRETER
How to start it:
./console.py

How to use it:
(List of Commands)
quit - Exit the program
EOF - Quit program
create - Create a new instance of BaseModel and print the id
show - Print the string representation of an instance
destroy - Delete an instance based on class name and id
all - Print all string representation of all instances
update - Update an instance based on the class name and id
count - Retrieve the number of instances of a class

Examples:
(hbnb) quit
(hbnb) EOF
(hbnb) create City
(hbnb) destroy City 636fef90-1cc6-46e8-a1e4-ebfb6d707660
(hbnb) all
(hbnb) update City 636fef90-1cc6-46e8-a1e4-ebfb6d707660
(hbnb) count City

AirBnB_clone

The goal of this project is to deploy on our server a simple copy of the AirBnB website.

The console is a Python interpreter that takes commands and runs  them
* How to start the console
`./console.py`
* How to use it
` (hbnb) <command> <arg1> ... <argn>
* Examples
`(hbnb) create BaseModel 93423-f323r-3342303-342`
`(hbnb) all BaseModel
`(hbnb) update User e5qr-131334-13413-1343 name "John Good"`
