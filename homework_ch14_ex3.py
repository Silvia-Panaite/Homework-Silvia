list = []

while True:
    number = int(input('Please type in a number: '))
    if number == '':
        break
    if number < 0:
        list = list + [number]
        list.sort()
        print('The list with negatives is: ')
        for item in list:
            print(' - ' + str(item))
    if number == 0:
        list = list + [number]
        list.sort()
        print('The list with 0 is: ')
        for item in list:
            print(' - ' + str(item))
    if number > 0:
        list = list + [number]
        list.sort()
        print('The list with positives is: ')
        for item in list:
            print(' - ' + str(item))



