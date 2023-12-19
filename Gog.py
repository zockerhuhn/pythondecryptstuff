originalstring = "AbdulgehtMilchholen"
vergleichstring = ["geht", "hol"]

def gollum(original, vergleich):
    Treffer = 0
    for i in vergleich:
        if i in original:
            Treffer += 1
    return(Treffer)

print(gollum(originalstring, vergleichstring))