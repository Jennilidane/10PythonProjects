name = input("Ingrese su nombre/s:")
date = input("Ingrese la fecha:")
address = input("Ingrese su dirección:")
goals = input("Ingrese su meta personal:")

if name.isalpha() :
    print("El valor debe ser una palabra")
else :
    print("Name: ", name)

if date.isalnum() :
    print("Solo valores alfanumericos")
else :
    print("Date: ", date)

if address.isalnum() :
    print("Solo valores alfanumericos")
else :
    print("Address: ",address)

if goals.isalnum() :
    print("Solo valores alfanumericos")
else :
    print("Goal: ", goals)