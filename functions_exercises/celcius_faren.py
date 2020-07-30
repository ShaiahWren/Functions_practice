def cel_to_f(celcius):
    temp_faren = (float(celcius) * 1.8) + 32
    return f"{temp_faren} F"

celcius = float(input("Enter temp in celcius: "))

print(cel_to_f(celcius))

