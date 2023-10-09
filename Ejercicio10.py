# Get user email address
email = input("¿Cuál es tu dirección de correo electrónico?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
output = "Su nombre de usuario es '{}' y su nombre de dominio es '{}'".format(user_name,domain_name)

# Display output message
print(output)