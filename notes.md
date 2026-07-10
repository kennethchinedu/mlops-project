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