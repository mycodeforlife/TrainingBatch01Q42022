start_num = 0
next_num = 1
max_num = 10
for i in range(0, max_num):
    if i < 2:
        result = i
    else:
        result = start_num+next_num
        start_num = next_num
        next_num = result
    print(result)