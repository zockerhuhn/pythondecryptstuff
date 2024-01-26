message = input("original Text:")
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'
walloftext = ''
listofwords = open("listofwords.txt").read()
listofwords = listofwords.split("\n")
treffer = []

def get_nth_key(dictionary, n):
  for i, key in enumerate(dictionary.keys()):
    if key == n:
        return i
  raise IndexError("dictionary index out of range") 

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
  original = original.lower()
  global letters
  distribution = [17.40,9.78,7.55,7.27,7.00,6.51,6.15,5.08,4.76,4.35,3.44,3.06,3.01,2.53,2.51,1.89,1.89,1.66,1.21,1.13,0.79,0.67,0.27,0.04,0.03,0.02]
  sortedletters = ["e","n","i","s","r","a","t","d","h","u","l","c","g","m","o","b","w","f","k","z","p","v","j","y","x","q"]
  origdistribution = {}
  overwritekey = {}
  bestscore = int(1) #set this to minimun amount of hits to count as valid
  best = ""
  for i in letters:
    hits = 0
    for x in original:
      if x == i:
        hits += 1
    origdistribution[i]=hits
    overwritekey[i]=None
  origdistribution = dict(sorted(origdistribution.items(), key=lambda item: item[1], reverse=True))
  print(origdistribution)
  key = []
  for i in range(0,26):
    key.append(1)
  while key[25] != 3:
    tempresult = ""
    #print(key)
    for i in original:
      if i in letters:
        if overwritekey[i] is None:
          tempresult += sortedletters[get_nth_key(origdistribution,i)+minmax(key[letters.index(i)]-1,int(0),int(25))]
        else:
          tempresult += overwritekey[i]
    temp=[]
    temp=compare(tempresult,best,bestscore)
    best = str(temp[0])
    bestscore = temp[1]
    print(tempresult)
    if temp[2] is not None:
      for char in temp[2]:
        overwritekey[char]= sortedletters[get_nth_key(origdistribution,char)+minmax(key[letters.index(char)]-1,int(0),int(25))]
    print(overwritekey)
    key[0]+=1
    try:
      while key.index(3) is not None:
        if (key.index(3) >= 7):
          print(str(key.index(3)+1))
          #if key.index(3) >= 13:
            #compare(tempresult,best,bestscore)
        key[key.index(3)+1] += 1
        key[key.index(3)] = 0
    except:
      pass

def minmax(value, minimum, maximum):
  """
  returns the Value if it is between the minimum and maximum
  returns min/maximum if value is beneath minimum/maximum
  """
  return (min(max(value, minimum), maximum))

def checktext(texttocheck):
  loop = 0
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
    #print(loop)
  treffer.append(amount)
  return [amount,alreadyhit]

def compare(tempresult,best,bestscore):
  temp = checktext(tempresult)[0]
  score = int(temp[0])
  words = temp[1]
  if score == bestscore:
    best += '\n' + tempresult
    print("added %s with %s matches" % (tempresult,score))
  elif score > bestscore:
    best = tempresult
    bestscore = score
    print("replaced %s with %s with %s matches" % (best,tempresult,score))
  return [best,bestscore,words]

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
  for i in splittedtext:
    checktext(i)
  #print(splittedtext)
  print("most matches (%s) in word: %s with key: %s/%s" % (max(treffer) ,splittedtext[(treffer.index(max(treffer)))], treffer.index(max(treffer))+1, treffer.index(max(treffer))-25))
  #print(treffer)
  input()
  splittedxyz = xyz(message)
else:
  if input("encrypt? [y/n]") == "y":
    print(gartenzaun_en(message))
  else:
    print(gartenzaun_de(message))