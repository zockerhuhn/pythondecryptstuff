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
    walloftext += result + ';'
    if key < 26:
        caeserdecrypt(original, (key+1))

def xyz(original):
  global letters
  result = ""
  key = []
  for z in range(len(letters)):
    key.append(int(0))
  while key[25] != 25:
    for i in original:
      num = letters.find(i)
      num += key[num]
      if num >25:
        num -= len(letters)
      result += letters[num]
    result += ';'
    key[0] += 1
    while 26 in key:
      key[key.index(26)+1] += 1
      key[key.index(26)] = 0
    #print(key)
    #print('\n')
  return result

def checktext(texttocheck):
    loop = 0
    for splitted in texttocheck:
        amount = 0
        alreadyhit = []
        for word in listofwords:
            loop += 1
            if len(word) >= 3:
                if word in splitted:
                    if word not in alreadyhit:
                        amount += 1
                        #print(word)
                        alreadyhit.append(word)
        #print(loop)
        treffer.append(amount)

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
    caeserdecrypt(message, 1)
    splittedtext = walloftext.split(';')
    checktext(splittedtext)
    #print(splittedtext)
    print("most matches (%s) in word: %s with key: %s/%s" % (max(treffer) ,splittedtext[(treffer.index(max(treffer)))], treffer.index(max(treffer))+1, treffer.index(max(treffer))-25))
    #print(treffer)
    splittedxyz = xyz(message).split(';')
    print(checktext(splittedxyz))
else:
    if input("encrypt? [y/n]") == "y":
        print(gartenzaun_en(message))
    else:
        print(gartenzaun_de(message))