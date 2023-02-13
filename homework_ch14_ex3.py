list_negatives = []
list_zeros = []
list_positives = []

while True:
    number = int(input('Please type in a number: '))   
    if number == ' ':
        break
    if number < 0:
        list_negatives = list_negatives + [number]
    elif number == 0:
        list_zeros = list_zeros + [number]
    elif number > 0:
        list_positives = list_positives + [number]

print(list_negatives)
print(list_zeros)
print(list_positives)



