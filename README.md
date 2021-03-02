# Movie-Theater-Seating

Language: Python

How to run the program: In order to run the program, the user wants to go to the directory where the theaterSeating.py file is stored and
run python3 theaterSeating.py "filepath". Here "filepath" is the full path of the input text file. The output of this will be the file
path of the output rows.

How to run the test: In order to run the tests, the user wants to go to the directory where the unitTests.py file is stored and run 
python3 unitTests.py. This program will output "All tests passed" if all tests have passed.

Assumptions: 
1. In the input file, the first reservations are appear first in the file.
2. The customers want to sit at the front of the theater.

How we maximize customer satisfication: 
1. The first customers to reserve get seats at the front of the theater.
2. The algorithm tries to put groups that sign up together into the same row with no spaces in between so that they can enjoy the movie together.

How we maximize customer safety:
1. Customers that are not in the same reservation request will have a buffer of three seats and/or one row. 
2. Even if customers are in the same group, we will have a buffer of one row so that not everyone is grouped extremely close together.

How we maximize theater size:
1. We start at the beginning of each column so that there are no leftover seats at the ends. 
2. We try to group the reservations together but if there are not enough seats in a row, then we will start to assign people to the
first avaliable seat.


