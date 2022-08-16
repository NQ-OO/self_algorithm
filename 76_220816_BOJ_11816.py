input_num = input()

if input_num[:2] == "0x" :
  print(int(input_num, 16))
elif input_num[:1] == "0" : 
  print(int(input_num, 8))
else : 
  print(int(input_num))
  
  

# print(input_num[:2])
  