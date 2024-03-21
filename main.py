from Lowstring import listofwords
message = "Diesisteinbeispielsatzfuerdiecaeserverschluesselung"
letters = 'abcdefghijklmnopqrstuvwxyz'
walloftext = []
def caeserdecrypt(original, key):
    global walloftext
    global letterswithkey
    letterswithkey = ''
    for letter in range(len(letters)):
        letterswithkey += (letters[(letter+key)%len(letters)])
    result = ""
    for symbol in original:
        if symbol in letters:
            result += letterswithkey[letters.find(symbol)]
    walloftext.append(result)
    if key < 26:
        caeserdecrypt(original, (key+1))

def checktext(texttocheck):
    amount = 0
    for word in listofwords:
        if word in texttocheck:
            amount += 1
    return amount

bestscore = 1
endresult = ""
caeserdecrypt(message.lower(), 1)
for sentence in walloftext:
    score = checktext(sentence)
    if score == bestscore:
        endresult += "\n" + sentence
    elif score > bestscore:
        endresult = sentence
        bestscore = score
print("most matches (%s) in word(s): \n %s" % (bestscore, endresult))