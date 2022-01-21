

file = open('titles.txt')

firstWordToTitle = {}
lastWordToTitle = {}

lines = file.readlines()
for title in lines:
    titleSplit = title.split(' ')
    lastWord = titleSplit[len(titleSplit)-1][:len(titleSplit[len(titleSplit)-1])-1]
    list = lastWordToTitle.get(lastWord, [])
    if title not in list:
        list.append(title[0:-1])
    lastWordToTitle[lastWord] = list
    list = firstWordToTitle.get(titleSplit[0], [])
    if title not in list:
        list.append(title[0:-1])
    firstWordToTitle[titleSplit[0][:len(titleSplit[0])]] = list
    
for key in firstWordToTitle.keys():
    
    for ending in firstWordToTitle[key]:
        ending = ending[ending.find(' ')+1:]
        if key not in lastWordToTitle.keys():
            continue
        for beginning in lastWordToTitle[key]:
            print(beginning + " " + ending)