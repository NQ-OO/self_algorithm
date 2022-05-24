
input_num = int(input())

def moo(cnt) : 
  if cnt == 1 : 
    return "moo"
  else : 
    cnt -= 1
    before = moo(cnt)
    second = "m"+"o"*(cnt+2)
    return before + second + before

print(moo(input_num))