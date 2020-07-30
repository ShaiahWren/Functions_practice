
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False



def is_odd(num):
    if is_even(num) != True:
        return True
    else:
        return False




def only_odds(my_list):
    odd_list = []
    for i in my_list:
        if is_odd(i) == True:
            odd_list.append(i)
        else:
            pass
    return odd_list

print(only_odds([11, 20, 42, 97, 23, 10])) 