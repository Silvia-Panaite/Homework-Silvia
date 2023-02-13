list_negatives = []
list_zeros = []
list_positives = []

while True:
    number = input('Please type in an integer number(blank if exit): ')
    if number == '':
        break
    else:
        number = int(number)
    if number < 0:
        list_negatives.append(number)
    elif number == 0:
        list_zeros.append(number)
    else: 
        list_positives.append(number)


print(list_negatives)
print(list_zeros)
print(list_positives)



