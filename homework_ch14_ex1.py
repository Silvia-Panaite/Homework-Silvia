list_ = []

while True:
    number = int(input('Please type in a number: '))
    if number == 0:
        break
    list_ = list_ + [number]

list_.sort()

print('The list is: ')
for item in list:
    print(' - ' + str(item))








