list = []

while True:
    number = int(input('Please type in a number: '))
    if number == 0:
        break
    list = list + [number]

list.sort()

print('The shopping list is: ')
for item in list:
    print(' - ' + str(item))








