import random

numero = random.randrange(1,50)
jugador = int(input("Adivine un numero entre el 1 al 50: "))

while jugador != numero :
    if jugador > 50 :
        print("Adivinaste un numero fuera del rango")
        jugador = int(input("\nIntenta otra vez: "))
    elif jugador < numero :
        print("Necesitas adivinar un numero mas alto.")
        jugador = int(input("\nAIntenta otra vez: "))
    else :
        print("Necesitas adivinar un numero mas bajo. Intenta otra vez")
        jugador = int(input("\nIntenta otra vez: "))

print("Adivinaste el numero correcto.")