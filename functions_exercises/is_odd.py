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

num = int(input("Enter a number: "))

print(is_odd(num))