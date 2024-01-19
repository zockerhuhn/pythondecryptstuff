from nltk.tokenize import sent_tokenize, word_tokenize

#message = input("original") #encrypted message
message = input("original Text:")
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'
walloftext = ''
listofwords = open("listofwords.txt").read()
listofwords = listofwords.split("\n")
treffer = []

def caeserdecrypt(original, key):
    global walloftext
    result = ""
    for symbol in original:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num += key
            if num >25:
                num -= len(LETTERS)
            result += letters[num]
        elif symbol in letters:
            num = letters.find(symbol)
            num += key
            if num >25:
                num -= len(letters)
            result += letters[num]
    print('key #%s: %s' % (key, result))
    walloftext += result
    walloftext += ';'
    if key < 26:
        caeserdecrypt(original, (key+1))

def checktext(texttocheck):
    loop = 0
    for splitted in texttocheck:
        amount = 0
        alreadyhit = []
        for word in listofwords:
            loop += 1
            if len(word) >= 3 and word in splitted and word not in alreadyhit:
                amount += 1
                print(word)
                alreadyhit.append(word)
        print(loop)
        treffer.append(amount)

def gartenzaun_en(text):
    text2 = text[::2]
    text3 = text[1::2]
    return text2 + text3

def gartenzaun_de(text):
    if len(text) / 2 != len(text) // 2:
        text += "_"
    middle = len(text) // 2
    text2 = ""
    for i in range(middle):
        text2 += text[i]
        text2 += text[i + middle]
    return text2

if input("caeser/gartenzaun [c/g]") == "c":
    caeserdecrypt(message, 1)
    splittedtext = walloftext.split(';')
    checktext(splittedtext)
    print(splittedtext[(treffer.index(max(treffer)))])
    print([word_tokenize(t) for t in sent_tokenize(splittedtext[(treffer.index(max(treffer)))], 'german')])
    print(treffer)
else:
    if input("encrypt? [y/n]") == "y":
        print(gartenzaun_en(message))
    else:
        print(gartenzaun_de(message))