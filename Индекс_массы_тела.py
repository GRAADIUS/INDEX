from math import *
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Ja mis su nimi on? ")
print(f"Meeldiv tutvuda {nimi}!")
või=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")

if int(või)==1:
    pikkus=input("sisestage oma pikkus ")
    mass=input("sisestage oma mass ")
    index=round((mass)/(0.01*int(pikkus))**2,1)
    print(f"{nimi}! Sinu keha indeks on: {index}")
    if int(index)<=16:
        print("Tervisele ohtlik alakaal")
    elif int(index)>16 and int(index)<=19:
        print("Alakaal")
    elif int(index)>19 and int(index)<=25:
        print("Normaalkaal")
    elif int(index)>25 and int(index)<=30:
        print("Ülekaal")
    elif int(index)>30 and int(index)<=35:
        print("Rasvumine")
    elif int(index)>35 and int(index)<=40:
        print("Tugev rasvumine")
    elif int(index)>40:
        print("Tervisele ohtlik rasvumine")
else:
    print("Kahju! See on väga kasulik info!")
    print()
print("Kohtumiseni, "+nimi+"! Igavesti Sinu, Python!")
