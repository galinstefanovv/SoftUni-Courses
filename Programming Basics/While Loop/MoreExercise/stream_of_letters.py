import re
word = input()
pattern = re.compile("[A-Za-z]+")
newWord = ""
c = False
o = False
n = False
while word != "End":
    if pattern.fullmatch(word) is not None:
        if word == "c":
            if c:
                newWord += word
            c = True
        elif word == "o":
            if o:
                newWord += word
            o = True
        elif word == "n":
            if n:
                newWord += word
            n = True
        else:
            newWord += word

        if c and o and n:
            print(newWord, end=" ")
            newWord = ""
            c = False
            o = False
            n = False
    word = input()

