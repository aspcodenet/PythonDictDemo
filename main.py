# mappa två värden   - kontonummer + saldo
#                       spelarnamn + jerseyNumber


theDict = {"V0":"S001", "VA": "S002", "VI": "S001", "VIR": "S005", "VII":"S005", "VV":"S009",
"VIII":"S007"}


for va in theDict.values():
    if va in uniqueValuesDicten:
        pass
    else:
        uniqueValuesDicten[va] = 0
    print(va)

# DYNAMISK DATASTRUKTUR
namnAntal = {}  # namn, antal
with open("namn.txt", "r") as filen:
    for raden in filen:
        radUtanNewLine = raden.replace("\n", "")
        if radUtanNewLine in namnAntal:
            namnAntal[radUtanNewLine] =  namnAntal[radUtanNewLine] + 1
        else:
            namnAntal[radUtanNewLine] = 1

for key in namnAntal.keys():
    print( key,  namnAntal[key] )           

for val in namnAntal.values():
    print( val )           

for key, value in namnAntal.items():
    print( key, value )






players = {}

players["foppa"] = ["Modo", "Colorado"]
players["mats"] = ["Nacka", "Djurgården", "Toronto"]

for key,value in players.items():
    print(key)
    for namn in value:
        print(f"     {namn}")
    


playerName = input("Ange ny player") #mats
if playerName in players:
    print("Finns redan")
else:
    jersey = int(input("Ange tröjnummer"))  #99
    players[jersey] = playerName




listan = [12,13,14,99]
listan.append(100)

for tal in listan:
    print(tal)


for i in range(0, len(listan)):
    print(listan[i])


del listan[2]    

for i in range(0, len(listan)):
    print(listan[i])
