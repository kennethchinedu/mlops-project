/usr/local/bin/python3

Python 3.13.7

Untracked files are files that have  not been recognized by git, git in itself is not aware thse file exist

staged files are changes prepared to go into our next commit 

config before commit informs git of he author, who is making and commiting the changes , the author

/usr/local/bin/python3

Now which python is running within the python inside the virtul environment on /Users/apple/Desktop/Mlops/project1/.venv/bin/python3

Almost nothing was in when i ran pip list firs time

certifi            2026.6.17
charset-normalizer 3.4.9
idna               3.18
pip                25.2
requests           2.34.2
urllib3            2.7.0

i moved back into my local directory after deativate

I dont thing .venv should be commited, it has a lot of things that can slow down push and make app larger

the == pins the package to a particular version 
certifi==2026.6.17
charset-normalizer==3.4.9
idna==3.18
requests==2.34.2
urllib3==2.7.0

Requirement.txt are packages needed to run the program, so they need to be commited so other environments running the program can see it too

I think you pin it for consistency because at the point of development the dependencies are consistent with oyour ap, you dnt want a break


both are server urls, one is used when pushing and another when pulling
I think the u means i want to push online and from this branch moving forward
.venv is not there 

i think origin is like the source i want to push and pull from
So basically a commit is a save snapshot, it like a save made in a time fraame and saved somewhere, ina history,so when i push a code, it take all the chains of canges made and copies it to the sever
eveything i did not push online is lost

TypeError
it works cus it converts the string 3 to int 3 by wrapping it inside the int function

input always returns string 
The first is a divider which returns float the other is a floor division which returns integer cutting off the other numbers and returns only the integer

List are mutable objects, you can loop, list and read them and write to them them
Dictionaries allows us to store key pair values, you can update a dictonary, use the get function to check if a key pair exists


https://www.geeksforgeeks.org/python/python-dictionary-get-method/
https://stackoverflow.com/questions/75653075/looping-through-a-list-of-dictionaries-defining-and-saving-the-variables-for-us
https://docs.python.org/3/tutorial/datastructures.html

Is None checks for identity and == checks for equality, that is a big different.

looping over a dictionary directly yields only its keys, while looping over .items() yields key-value pairs as tuples
The print statement loops over and return zero values for the list, it means the list exists but the context of the check is returning nothing, in fact printing just zero values is misleading, it does not give full context on what exactly is happening

The first function takes a  list of dictionaries, breaks it up and returns variables, that the secod ine can ready

The second function takes in list of variables row_count, missing_name, missing_age, missing_city that the first function returned and write some texts about it, saying how many rows is here and here based on what the first function returned 

Parameters are the placeholders inside the function definition, while arguments are the actual values you pass into the function when you call it

variables defined in functions are called local variables, they can't be used outside, why that matters? So the right variable is scoped to the right places to avoid missing variables

An empty function returns None to the computer's memory, while a print() statement inside a function sends text to the human screen.


>>> try:
...     ken["city"]
...     "ken".items()
... except KeyError:
...     print("my dictionary has not such key")
...     
my dictionary has not such key

My finding is that it only catches the exceptions specified in the block, other failed exceptions are not caught



When attempting `ken["city"]`, it accurately catches the missing key.

When running `"ken".items()`, it lets the program crash with an `AttributeError`. This is the correct behavior because a string attribute error is fundamentally different from a missing dictionary key.


When running "ken".items(), the bare except completely silences the AttributeError


Raised means an error occurs and Python throws an exception. Handled means an except block catches the exception so the program can continue.

Catching a specific exception avoids hiding unrelated bugs. A bare except: can accidentally catch unexpected errors like TypeError, NameError, or even KeyboardInterrupt.

Yes. A finally block runs whether or not an exception occurs. It's used for cleanup tasks, such as closing files, releasing resources, or disconnecting from a database.