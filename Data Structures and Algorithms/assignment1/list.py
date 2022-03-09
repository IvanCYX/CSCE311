class myList(list):

    #function to add length of list and string
    def add(self, other):
        return len(self) + len(other)

    #function to multiply length of list and string
    def multiply(self, other):
        return len(self) * len(other)

x = myList(['h', 'e', 'l', 'l', 'o'])

print(myList.add(x, 'universe'))
print(myList.multiply(x, 'universe'))
