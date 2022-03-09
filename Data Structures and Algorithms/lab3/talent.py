f = open ('input.txt')
file = f.read()
content = file.splitlines()


#create empty dictionary object instance
celeb = {}
idList = []
duplicates = []

for line in content:
    #continue of the first character is ID
    if line[:2] == "ID":
        continue

    else:
        #split by /t (got from printing output)
        s = line.split("\t")
        stripped = []

        for i in s:
            word = i.strip()
            stripped.append(word)

        idList.append(stripped[0])
        celeb[stripped[0]] = stripped[1:5]

for key in celeb:
    print(key, celeb[key], "\n")

myList = sorted(idList)
for i in myList:
    if myList.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print("Celebrities who are double talented are: ", duplicates)


