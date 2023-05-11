## Task 3: 2023-05-09

1. The `uuid` module
- UUID stands for __Universally Unique Identifier__
- The uuid module defines some constants, a class `uuid.UUID` and other methods/functions.
- A UUID is a 128-character string of alphanumeric variable type, that uniquely identifies an object entity of resource in both space and time of a table.
- The uuid.UUID class can be used to create UUID in 5 different ways by passing an argument to an instance of the class either of the following:
	* a string of 32 hexadecimal digits: `hex` argement
	* a string of 16 bytes in big-endian order: `bytes` argument
	* a string of 16 bytes in little-endian order: `bytes_le` argument
	* a tuple of 6 integers: `fields` argument
	* a single 128-bit integer: `int` argument
- The uuid module has 4 functions for generating UUID as specified in RFC4122
	* `uuid.uuid1()`
	* `uuid.uuid3()`
	* `uuid.uuid4()`
	* `uuid.uuid5()`
- The `uuid4()` was used in this project because it generates a secure random identifier compared to `uuid3()` and `uuid5()`
- A UUID can be converted to a string object by passing the UUID to Python's builtin `str()` function like this, `str(uuid)`

----------------------------------------------------

2. The `datetime` module
- The datetime module supplies classes for manipulating dates and time.
- This module defines some constants and also some classes among which are:
	* `datetime.date`
	* `datetime.time`
	* `datetime.datetime`
	* `datetime.timedelta`
	* `datetime.timezone`
- Each class object contains corresponding various attributes, properties or methods.
- The datetime.datetime object is a single object containing all the information froma a date object and a time object. Hence, its use.
- Two ways to get the current local date and time
	* from datetime import datetime
	* datetime.today() which is equivalent to:
	* datetime.fromtimestamp(time.time())
	* datetime.now() which can provide more details than the other method
	```
- A datetime object can be converted to a string using the `.isoformat()` method on the datetime object. This method takes two optional arguments `sep="T"` and `timespec="Auto"`. The sep is the character to print in between the date and the time while the timespec specifies the additional component of the time to include after the date.

----------------------------------------------------
3. The `__class__` and `__dict__` attributes of a class object
- Every Python class has a __dict__ attribute that contains a dictionary of its instance attributes.
- The __dict__ attribute of a class can be seen by calling the Python's builtin `var()` function on the class instance or by accessing the __dict__attribute using a dot notation.
- New elements can be added to a class' __dict__ attrubute using the `update()` function and passsing a key value pair to it like this.
	* self.__dict__.update({"new_key": new_value})
- The name of a class in Python can be accessed from an instance by accessing the class' name attribute from the instance like this.
	* self.__class__.__name__
