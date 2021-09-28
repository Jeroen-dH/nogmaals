# name of student: Jeroen de Heer 
# number of student: 99068895
# purpose of program: geld ruilen
# function of program: geld ruilen
# structure of program: python

toPay = int(float(input('Amount to pay: '))* 100) # Geld wat je moet betallen 
paid = int(float(input('Paid amount: ')) * 100) #geld wat jij geeft
change = paid - toPay # wat je terug moet krijgen
aantal = "aantal: "

if change > 0: # iets terug moet geven
  coinValue = 500 # wat je terug moet geven
  
  while change > 0 and coinValue > 0: # als ze alle 2 boven 0 zijn
    nrCoins = change // coinValue #

    if nrCoins > 0: # numer van coins die je terug moet geven
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # totaal van wat je terug moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hoeveel je hebt terug gegeven
      change -= nrCoinsReturned * coinValue # coins terug gegeven * coinvalue
    
    aantal =  str(aantal) + str(nrCoins) + ' van '+ str(coinValue) + ' cents. '
# comment on code below: Alle geld eenheeden in centen
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #als je niet genoeg geld terug krijgt
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
print (aantal)