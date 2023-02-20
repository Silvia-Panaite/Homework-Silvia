fruits = [apples, [apples, oranges], [apples, oranges, bananas apples], [oranges, bananas, lemons]]
def list_thing(fruits):
    new_string = ''
    for i in list:
        new_string = new_string + str(i)
        if list.index(i) == (len(list)-2):
            new_string = new_string + ', and '
        elif list.index(i) == (len(list)-1):
            new_string = new_string
        else:
            new_string = new_string + ', '
    return new_string

print (list_thing(spam))