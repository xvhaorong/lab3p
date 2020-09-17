# Author: Haorong Xu hxx5086@psu.edu 
# Collaborator: 
# Collaborator: 
# Section: 12
# Breakout: 

def sum_n(n):
  if (n>0):
    return n+sum_n(n-1)
  else:
    return n

def print_n(s,n):
  if(n>0):
    print(f"{s}");
    return print_n(s,n-1)

def run():
  num=int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  a=input("Enter a string: ")
  print_n(a,num)

if __name__=="__main__":
  run()