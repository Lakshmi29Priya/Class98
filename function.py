def countWordsFromFile():
    fileName= input("Enter the file name: ")
    numberOfWords=0
    characterCount=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
        characterCount=characterCount+len(line)


    print("Number of words:")
    print(numberOfWords)
    print("Number of characters:")
    print(characterCount)
countWordsFromFile()         