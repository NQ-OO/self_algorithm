# https://www.acmicpc.net/problem/1991
import sys
input = sys.stdin.readline

input_num = int(input())
node_dict = {}
for int in range(input_num) : 
  root_node, left, rigth = list(input().split())
  node_dict[root_node] = [left, rigth]

def preorder(root) : 
  if root  == '.' : 
    return
  else : 
    print(root, end= "")
    preorder(node_dict[root][0])
    preorder(node_dict[root][1])
    
def inorder(root) : 
  if root  == '.' : 
    return
  else : 
    inorder(node_dict[root][0])
    print(root, end= "")
    inorder(node_dict[root][1])

def postorder(root) : 
  if root  == '.' : 
    return
  else : 
    postorder(node_dict[root][0])
    postorder(node_dict[root][1])
    print(root, end= "")

    
preorder("A")
print()
inorder("A")
print()
postorder("A")