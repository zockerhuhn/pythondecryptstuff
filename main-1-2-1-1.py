import numpy
rekursion = None
unknownrekursion = None
rekursiv = None
#eee = "test;goblin;e"
listofwords = open("listofwords2.txt").read().split("/n")
print(listofwords)
#listofwords = eee.split(";")5

def caeser(original, verschiebung):
    result = ""
    for i in range(len(original)):
        char = original[i]
        if char.isupper():
            result += chr((ord(char) + verschiebung-65) % 26 + 65)
        else:
            result += chr((ord(char) + verschiebung-97) % 26 + 97)
    return result

def caeserrek(original, verschiebung, rekursion, decryptrekursion):
    result = ""
    if rekursion == 0:
        try:
            for x in range(26):
                verschiebung2 = verschiebung
                #result = ""
                for i in range(len(original)):
                    char = original[i]
                    if char.isupper():
                        result += chr((ord(char) + verschiebung2-65) % 26 + 65)
                    else:
                        result += chr((ord(char) + verschiebung2-97) % 26 + 97)
                    if decryptrekursion:
                        verschiebung2 += -rekursion
                    else:
                        verschiebung2 += rekursion
                rekursion += 1
                result += "\n"
        except:
            pass
    else:
        for i in range(len(original)):
            char = original[i]
            if char.isupper():
                result += chr((ord(char) + verschiebung-65) % 26 + 65)
            else:
                result += chr((ord(char) + verschiebung-97) % 26 + 97)
            if not rekursion == None:
                if decryptrekursion:
                    verschiebung += -rekursion
                else:
                    verschiebung += rekursion
    return result

def gartenzaun_en(text):
    text2 = text[::2]
    text3 = text[1::2]
    return text2 + text3

def gartenzaun_de(text):
    if not (len(text)/2) == (len(text)//2):
        text += "_"
    middle = len(text) // 2
    text2 = ""
    for i in range(middle):
        text2 += text[i]
        text2 += text[i + middle]
    return text2

def checkstring(original):
    teststring = ""
    brokenupstring = numpy.array([original.split("\n")])
    Treffer = numpy.full_like(brokenupstring, 0)
    for i in range(len(brokenupstring[0])):
        for z in range(len(listofwords)):   
            if listofwords[z] in brokenupstring[0, i]:
                if len(listofwords[z]) >= 2:
                    teststring += listofwords[z] + ";"
                    #Treffer[0, i] = int(Treffer[0, i]) + 1
                    Treffer[0, i] += 1
    print(original)
    #print(listofwords)
    #print(brokenupstring)
    #print(Treffer)
    print("most matches in word: " + str(brokenupstring[0, numpy.argmax(Treffer)]) + ", with " + str(max(Treffer[0])) + " matches")
    print(teststring)


while 1:
    print("original text:")
    original = input()
    print("Caesar/Garten [c/g]")
    method = input()
    if method == "c":
        print("verschiebung:")
        verschiebung = int(input())
        print("rekursiv? [y/n]")
        if input() == "y":
            rekursiv = True
            print("Rekursion:")
            rekursion = int(input())
            print("decrypt? [y/n]")
            if input() == "y":
                decryptrekursion = True
            else:
                decryptrekursion = False
        else:
            rekursiv = False
        if verschiebung == 0:
            if rekursiv:
                toprint = ""
                for i in range(25):
                    verschiebung += 1
                    toprint += "Cipher" + str(i+1) + "/" + str(25 - i) + ":"  + caeserrek(original,verschiebung,rekursion,decryptrekursion)
                    toprint += "\n"
                    toprint += "---"
                    toprint += "\n"
            else:   
                toprint = ""
                for i in range(25):
                    verschiebung += 1
                    toprint += "Cipher" + str(i+1) + "/" + str(25 - i) + ":"  + caeser(original,verschiebung)
                    toprint += "\n"
                    toprint += "---"
                    toprint += "\n"
        else:
            if rekursiv:
                toprint = ""
                toprint += "Cipher: " + caeserrek(original,verschiebung,rekursion,decryptrekursion)
            else:
                toprint = ""
                toprint += "Cipher: " + caeser(original,verschiebung)
        checkstring(toprint)
    if method == "g":
        print("decrypt? [y/n]")
        if input() == "y":
            print(gartenzaun_de(original))
        else:
            print(gartenzaun_en(original))
input()