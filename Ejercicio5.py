palabra = "a ante bajo contra de desde durante en entre lo la li lu le sin sobre tras mediante hasta hacia para por según traso una uno unos unas y e ni que o u pero"
palabra = palabra.split()
frase =input("Ingrese la frase: ")
frase = frase.split()
sig = []
for palabras in frase :
    if palabras not in palabra :
        sig.append(palabras[0])
sig = "".join(sig)
sig=sig.upper()
print("El acronimo es: ",sig)