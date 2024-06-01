# List Comprehensions

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # map() can listify the list of strings individually
'''
'''
output=[]
     for x in range(n):
         for y in range (n):
             for z in range (n):
                 output.append([x,y,z])
                 print(output)
 '''
'''
print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
'''
'''
output=[[x,y,z] x for x in range() y for y in range() z for z in range()]
print (output)
'''
'''
result=[[i,j,k] for i in range(x) for j in range(y) for k in range(z) if x+y+z != 0]
print(result) #[0,0,0]

result=[[i,j,k] for i in range(x+1) for j in range(y) for k in range(z) if x+y+z != n]
print(result)#[[0,0,0],[0,0,1]
'''
#result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z) if x+y+z != 0]
#print(result)# [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]

#result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if x+y+z != 0]
#print(result)# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

#result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if x+y+z != 0]
#print(result)
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]

#result=[[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n]
#print(result)#[0,0,0]

#result=[[i,j,k] for i in range(x+1) for j in range(y) for k in range(z) if i+j+k != n]
#print(result)#[[0, 0, 0], [1, 0, 0]]

#result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z) if i+j+k != n]
#print(result)#[[0, 0, 0], [1, 0, 0]]
              #[[0, 0, 0], [0, 1, 0], [1, 0, 0]]

#result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
#print(result)
#[[0, 0, 0], [1, 0, 0]]
#[[0, 0, 0], [0, 1, 0], [1, 0, 0]]
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]




if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # map() can listify the list of strings individually

result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(result)
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
