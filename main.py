message = "Diesisteinbeispielsatz" #input("original Text:")
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'
walloftext = ""
listofwords = open("listofwords.txt").read()
listofwords = listofwords.split("\n")
loop = 0

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
    #print('key #%s: %s' % (key, result))
    walloftext += result + ';'
    if key < 26:
        caeserdecrypt(original, (key+1))

def checktext(texttocheck):
    global loop
    amount = 0
    alreadyhit = []
    for word in listofwords:
        loop += 1
        if len(word) >= 3:
            if word in texttocheck:
                if word not in alreadyhit:
                    amount += 1
                    #print(word)
                    alreadyhit.append(word)
    return amount

def gartenzaun_en(text):
    return text[::2] + text[1::2]

def gartenzaun_de(text):
    if " " in text:
        text = text.replace(' ', '')
    if not (len(text) % 2 == 0):
        text += "_"
    middle = len(text) // 2
    text2 = ""
    for i in range(middle):
        text2 += text[i]
        text2 += text[i + middle]
    return text2

if "c" == "c":
    bestscore = 1
    endresult = ""
    caeserdecrypt(message, 1)
    splittedtext = walloftext.split(';')
    for sentence in splittedtext:
        score = checktext(sentence)
        if score == bestscore:
            endresult += "\n" + sentence
        elif score > bestscore:
            endresult = sentence
            bestscore = score
    #print(splittedtext)
    print("most matches (%s) in word(s): \n %s" % (bestscore, endresult))
else:
    if input("encrypt? [y/n]") == "y":
        print(gartenzaun_en(message))
    else:
        print(gartenzaun_de(message))