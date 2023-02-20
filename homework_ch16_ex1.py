#In this exercise, you will create a program that reads words from the user until the user enters a blank line.
#After the user enters a blank line your program should dis- play each word entered by the user exactly once.
#The words should be displayed in the same order that they were first entered.
# Read a collection of words entered by the user.
# Display each word entered by the user only
# once, in the same order that the words were entered.
# Read words from the user and store them in a list

input_list  = []
word = input("Enter a word (blank line to quit): ")
while True:
    if word == "":
        break
    if word not in input_list:
        input_list.append(word)
    word = input("Enter a word (blank line to quit): ")

for word in input_list:
    print (word)