list_negatives = []
list_zeros = []
list_positives = []

while True:
    number = int(input('Please type in a number: '))
    if number < 0:
        list_negatives.append(number)
    elif number == 0:
        list_zeros.append(number)
    elif number > 0:
        list_positives.append(number)
    else:
        number = input('Please type in a number: ') 
        break

print(list_negatives)
print(list_zeros)
print(list_positives)



