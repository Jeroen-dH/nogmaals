dag = input("Welke dag van de week is het: ")

if dag == "maandag":
    dag = 1
if dag == "dinsdag":
    dag = 2
if dag == "woensdag":
    dag = 3
if dag == "donderdag":
    dag = 4
if dag == "vrijdag":
    dag = 5
if dag == "zaterdag":
    dag = 6
if dag == "zondag":
    dag = 7
a = 1
while a <= dag:
    if a == 1:
        dag2 = "Maandag"
    if a == 2:
        dag2 = "Dinsdag"
    if a == 3:
        dag2 = "Woensdag"
    if a == 4:
        dag2 = "Donderdag"
    if a == 5:
        dag2 = "Vrijdag"
    if a == 6:
        dag2 = "Zaterdag"
    if a == 7:
        dag2 = "Zondag"
    print(dag2)
    a = a + 1