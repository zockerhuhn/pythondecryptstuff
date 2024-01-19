message = input("original Text:")
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
    print('key #%s: %s' % (key, result))
    walloftext += result + ';'
    if key < 26:
        caeserdecrypt(original, (key+1))

def xyz(original):
    global letters
    result:list
    best = ""
    bestscore = 1
    key = []
    for z in range(len(letters)):
        key.append(int(0))
    while key[25] != 25:
        result = ""
        for i in original:
            num = letters.find(i)
            num += key[num]
            while num > 25:
                num -= len(letters)
            result += letters[num]
        score = checktext(result)
        if score == bestscore:
            best += '\n' + result
            print("added %s with %s matches" % (result,score))
        elif score > bestscore:
            best = result
            print("replaced %s with %s with %s matches" % (best,result,score))
        key[0] += 1
        try:
            while key.index(26) != None:
                if (key.index(26) >= 2):
                    print(str(key.index(26)+1))
                key[key.index(26)+1] += 1
                key[key.index(26)] = 0
        except:
            pass
        #print(key)
        #print('\n')
    export = [best, bestscore]
    return export

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

if input("caeser/gartenzaun [c/g]") == "c":
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
    if input("xyz? [y/n]") == "y":
        export = xyz(message)
        print("most matches (%s) in: \n %s" % (export[1], export[0]))
else:
    if input("encrypt? [y/n]") == "y":
        print(gartenzaun_en(message))
    else:
        print(gartenzaun_de(message))