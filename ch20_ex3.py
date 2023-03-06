def main():
    #We create a dict but leave it blank for now
    letterDict = {}
    text = input("Enter a text string: ")
    for c in text:
        #We don't want to count non alphabetic characters
        if c.isalpha():
            #We don't need to count how many times we have seen this item so just store any
            #value using the current character as a key
            letterDict[c] = 1
    #Now len(letterDict) will return the number of items in the dict and that is also 
    #the number of unique characters
    print("The number of unique characters in that string = ", len(letterDict))

if __name__ == '__main__':
    main()