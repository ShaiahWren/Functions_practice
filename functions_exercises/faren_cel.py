def faren_to_c(faren):
    temp_celcius = (float(faren) - 32) * (5/9)
    return "%.2f F" % temp_celcius

faren = float(input("Enter temp in farenheight: "))

print(faren_to_c(faren))