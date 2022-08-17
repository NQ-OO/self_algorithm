input_num_cnt = input()
first_input_set = set(input().split(" "))
second_input_set = set(input().split(" "))

print(len(first_input_set-second_input_set) + len(second_input_set-first_input_set))



