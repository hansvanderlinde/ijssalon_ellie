prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5}
aanbieding = prijzen ["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst [:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for e1 in reclame_tekst4:
    if len(e1) < 5:
        print (e1.lower())
    else:
        print (e1.upper())
