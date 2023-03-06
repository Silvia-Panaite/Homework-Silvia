def main():
    letterDict = {}
    text = input("Enter a text string: ")
    for c in text:
        if c.isalpha():
            letterDict[c] = 1
    print("The number of unique characters in that string = ", len(letterDict))

if __name__ == '__main__':
    main()