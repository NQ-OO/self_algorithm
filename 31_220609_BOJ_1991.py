#50
import sys
input = sys.stdin.readline

input_cnt = int(input())
node_dict = {}
for _ in range(input_cnt) : 
  input_lst = input().split()
  node_dict[input_lst[0]] = [input_lst[1], input_lst[2]] 
  

def pre_traversal(root) : 
  if root == '.' : 
    return
  else : 
    print(root, end = "")
    pre_traversal(node_dict[root][0])
    pre_traversal(node_dict[root][1])
    
def in_traversal(root) : 
  if root == '.' : 
    return
  else : 
    in_traversal(node_dict[root][0])
    print(root, end = "")
    in_traversal(node_dict[root][1])
    
def post_traversal(root) : 
  if root == '.' : 
    return
  else : 
    post_traversal(node_dict[root][0])
    post_traversal(node_dict[root][1])
    print(root, end = "")


root = "A"
pre_traversal(root)
print()
in_traversal(root)
print()
post_traversal(root)