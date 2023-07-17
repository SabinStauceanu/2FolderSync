In this project I created one-way syncronisation method between 2 folders using python.
Firstly you must create an folder as an source and have some files in it (if you dont you can create files using my code) and an replica file, is up to you how you name these folders.
In this project I implemented the copy files method, create file method , delete file method and timed syncronisation method.
These methods are not accesible through running the compiler and are accesible via command line.
If you want to access one of the methods you have the next commands:
COPY:  py .\main.py --s -s sourcepath -r replicapath
CREATE:  py .\main.py --c -s sourcepath -r replicapath filename
DELETE:  py .\main.py --d -s sourcepath -r replicapath filename
TIMED SYNC: py .\main.py --t -s sourcepath -r replicapath time(seconds)
Note that creation and deleteing an file is only viable in the source folder and after that the syncronisation happens as intended.
