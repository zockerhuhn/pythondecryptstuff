def erzeugeSchluessel(schluesselwort):
    schluessel=""
    schluesselwort = schluesselwort.upper()
    for i in range(len(schluesselwort)):
        if schluesselwort[i] in schluessel:
            pass
        else:
            schluessel += schluesselwort[i]
    for i in range(25,-1,-1):
        zeichen=chr(i+65)
        if zeichen in schluessel:
            pass
        else:
            schluessel += zeichen
    return schluessel


print (erzeugeSchluessel("AABBCCDEFFF"))