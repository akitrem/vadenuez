import json

# Leer el archivo de texto plano
with open('variables_original.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Crear un diccionario vacío para almacenar los datos
data = {}

# Iterar sobre cada línea del archivo y agregar los datos al diccionario
for line in lines:
    key, value = line.split('=')
    data[key.strip()] = value.strip().replace("'", "")  # Eliminar comillas simples

# Convertir el diccionario a JSON y escribirlo en un archivo
with open('var4.json', 'w') as f:
    json.dump(data, f, indent=4)
