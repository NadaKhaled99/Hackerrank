# Loops

#Loops are control structures that iterate over a range to perform a certain task. They can work with any iterable type, such as lists and dictionaries. To control the loop in this problem, use the range function (see below for a description).
#There are two kinds of loops in Python.

#A for loop:

#for i in range(0, 5):
 #   print (i)

#And a while loop:

#i = 0
#while i < 5:
 #   print (i)
  #  i += 1

# Read an integer N. For all non-negative integers i < N, print i**2.

# Input Format
# The first and only line contains the integer, N.

# Constraints
# 1 <= N <= 20

# Output Format
# Print N lines, one corresponding to each i.

# Enter your code here. Read input from STDIN. Print output to STDOUT

#n = 0                      | it can start from 1 ---> n=1
#                           |
#                           |
#                           |
#                           |
#while n < 5:
 #   print (n)         ---> 0,1,2,3,4
  #  n += 1
#------------------------------------------
#for i in range(0, 5):
 #   print (i)           ---> 0,1,2,3,4

for i in range(0, n): 
   print(i**2)

#OR
    
i=0
while i<n:
    print(i**2)
    i=i+1

 
