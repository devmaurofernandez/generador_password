import random
import string

def generate_password(length=16):
    # Define los caracteres posibles para la contraseña
    characters = string.ascii_letters + string.digits + string.punctuation

    # Genera una contraseña aleatoria
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ejemplo: Genera una contraseña de longitud predeterminada (12 caracteres)
print("Contraseña generada:", generate_password())

