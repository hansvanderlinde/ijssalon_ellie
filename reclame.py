from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs - prijs * korting
    string1 = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    uitvoer = string1[:87]+",60 euro."
    return uitvoer

print (aanbieding_1("aardbei", 4, 0.1))

print()

def inkomsten_totaal (inkomsten, btw):
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = 0
    btw = 0.09
    for bedr in inkomsten:
        totaal = totaal + bedr
    btw = btw * totaal
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer    
print (inkomsten_totaal("inkomsten", "btw"))

print()

def laag_en_hoog (mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    return min(mijn_lijst), max(mijn_lijst)
print (laag_en_hoog("mijn_lijst"))

print()

def gemiddelde (mijn_lijst):
    fipd = [220, 430, 125, 160, 205, 90, 345]
    totaal = 0
    for bedr in fipd:
        totaal += bedr
    c = totaal / 7
    string1 = f"De gemiddelde inkomsten deze week zijn {c} euro."
    return string1[:42]+",00 euro"
print (gemiddelde("mijn_lijst"))

print()

def meervoudig(invoer_lijst):
    invoer_lijst = [10,5,3,2,1,2,9]
    laag_en_hoog (invoer_lijst)
    return max(invoer_lijst), min(invoer_lijst)
print (meervoudig("invoer_lijst"))

print ()

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print (combinatie("ïnvoer_lijst_2"))

