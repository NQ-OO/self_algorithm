



def recur(L) : 
  if L == word_len : 
    result_lst.append("".join(result))
  else : 
    for idx in range(len(card)) : 
        result[L] = card[idx]
        recur(L+1)
        

input_word = input()

card = ["A", "E", "I", "O", "U"]
visited = [0]* len(card)
result_lst = []
cnt = 0

for word_len in range(1, len(card)+1) :
  result = [0] * word_len
  recur(0)
  
result_lst.sort()
# print(result_lst)
print(result_lst.index(input_word)+1)




      