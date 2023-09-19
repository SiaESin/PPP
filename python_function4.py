#1 Function called max_num()to find the maximum of three numbers.
def max_num(x, y, z):
  return max([x, y, z])

print (max_num(15, 18, 22))


#2 Function called mult_list() to multiply all the numbers in a list.
def mult_list(myList):
  # return myList
  result = 1
  for x in myList:
    result = result * x
  return result

# list1 = [ 7, 17, 27]
print(mult_list([ 7, 17, 2]))

 



#3 Function called rev_string() to reverse a string.
def rev_string(txt):
 
  return txt [::-1]

print(rev_string("gnirts esrever"))



           
#4 Function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(n, a, b):
    if a <= n <= b:
        print(n, "This is true", a, "-", b)
    else:
        print(n, "This is false", a, "-", b)


print(num_within(3,2,4))



#5 Function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
  rows = [1]
  y = [0]
  for x in range(n):
    print(rows)
    rows=[left+right for left,right in zip(rows+y, y+rows)]
  return n>=1

print(pascal(8))