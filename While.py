my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
str_len = len(my_list)
index_str = 0
while str_len != 0:
    if my_list[index_str] > 0:
        if my_list[index_str] == 0:
            continue
        print(my_list[index_str])
    if my_list[index_str] < 0:
        break
    index_str = index_str + 1
    str_len = str_len - 1



