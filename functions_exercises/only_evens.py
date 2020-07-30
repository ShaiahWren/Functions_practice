def only_evens(my_list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list



print(only_evens([11, 20, 42, 97, 23, 10])) 