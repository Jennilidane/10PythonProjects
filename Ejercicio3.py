palabras = input("¿Que tiene en mente?")
palabra = palabras.split()
cont = 0
for i in palabra :
    cont+=1
print("Muy bien, tu me has mostrado tu pensamiento en ",format(str(cont))," palabras")