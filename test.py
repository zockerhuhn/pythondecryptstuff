def listwords(lenThreshold):
  numbers = [1,2,3,4,5,6,7,8,9,0]
  hasNumbers: bool
  originalList = (open("listofwords.txt").read()).split("\n")
  newList = []
  for word in originalList:
    hasNumbers = False
    if (len(word) >= lenThreshold) and (word not in newList):
      #print(word)
      for number in numbers:
        if str(number) in word:
          hasNumbers = True
          break
      if hasNumbers:
        continue
      newList.append(word)
  print("old file length: %s \n new file length: %s" % (len(originalList), len(newList)))
  return newList

list1 = listwords(2)
list2 = listwords(3)

matches = set(list1).difference(set(list2))
print(matches)
print(str(len(matches)))
with open("listofwords.txt", "w") as file:
  file.write("\n".join(list2))
