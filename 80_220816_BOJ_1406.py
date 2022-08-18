input_str = list(input())
input_command_cnt = int(input())

max = len(input_str)
cursor = max
for idx in range(input_command_cnt) : 
  command = input()

  if command[0] == "L" : 
    if cursor > 0 : 
      cursor -= 1 
  elif command[0] == "D" : 
    if max > cursor: 
      cursor += 1 
  elif command[0] == "B" : 
    if cursor >= 1: 
      del input_str[cursor-1]
      cursor -= 1
  elif command[0] == "P" : 
    input_str.insert(cursor, command[2])
    cursor += 1
print("".join(input_str))
    