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

def substitution(klartext, schluesselwort):
    schluessel = erzeugeSchluessel(schluesselwort)
    klartext = klartext.upper()
    geheimtext = ""
    for i in range(len(klartext)):
        zeichen = klartext[i]
        index = ord(zeichen)-65
        geheimbuchstabe = schluessel[index%26]
        geheimtext += geheimbuchstabe
    return(geheimtext)

print (substitution("DIES IST EIN ZUFAELLIGER BEISPIELSATZ","Platon"))
print (erzeugeSchluessel("Platon"))