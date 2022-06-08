

import sys 
input = sys.stdin.readline
    
input_dict = {} 
for _ in range(int(input())) :
  single_input = input().split()
  input_dict[single_input[0]] = [single_input[1], single_input[2]]
# print(input_dict)

def pre_traversal(start) :
  if start != '.' : 
    print(start, end="")
    pre_traversal(input_dict[start][0])
    pre_traversal(input_dict[start][1])
  
    

def in_traversal(start) :
    if start != '.' : 
      in_traversal(input_dict[start][0])
      print(start, end="")
      in_traversal(input_dict[start][1])
  
def post_traversal(start) :
    if start != '.' : 
      post_traversal(input_dict[start][0])
      post_traversal(input_dict[start][1])
      print(start, end="")

  
  
pre_traversal("A")
print()
in_traversal("A")
print()
post_traversal("A")
  
  
  

  