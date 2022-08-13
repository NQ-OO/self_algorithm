
board = [[1 for y in range(1000)] for x in range(1000)] 

  # "명령어를 받아서 parse 한다."
def get_order(order) : 
  parsed_order = order.split()
  x1, y1 = [int(parsed_int) for parsed_int in parsed_order[1].split(',')]
  x2, y2 = [int(parsed_int) for parsed_int in parsed_order[3].split(',')]
  target_lst = []
  for x_coordinate in range(x1, x2+1) : 
    for y_coordinate in range(y1, y2+1) : 
      target_lst.append([x_coordinate, y_coordinate])
  return (parsed_order[0], target_lst)



def take_order(command, target_lst) : 
  if command == "front" :
    for target in target_lst : 
      board[target[0]][target[1]] = 1
  elif command == "back" : 
    for target in target_lst : 
      board[target[0]][target[1]] = 0
  elif command == "flip" :
    for target in target_lst : 
      if board[target[0]][target[1]] == 0 :
        board[target[0]][target[1]] = 1 
      else:
          board[target[0]][target[1]] = 0
          
          
        

flag = True
while flag : 
  order = input()
  if not order :
    total = 0
    for row in board : 
      total += sum(row)
    print(total)
    break
  command, target_lst = get_order(order)
  take_order(command, target_lst)

