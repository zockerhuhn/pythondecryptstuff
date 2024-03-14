message = "Diesisteinbeispielsatzfuerdiecaeserverschluesselung"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'
walloftext = []
listofwords = (open("listofwords.txt").read()).split("\n")
def caeserdecrypt(original, key):
    global walloftext
    result = ""
    for symbol in original:
        if symbol in letters:
            num = (letters.find(symbol)+key)%len(letters)
            result += letters[num]
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