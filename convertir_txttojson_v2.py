import json

# Leer el archivo de texto plano

archivo=input("##########  dame el nombre del archivo:  " )
with open(archivo, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Crear un diccionario vacío para almacenar los datos
data = {}

# Iterar sobre cada línea del archivo y agregar los datos al diccionario
for line in lines:
    if '=' in line and not line.startswith('#'):
        key, value = line.split('=')
        data[key.strip()] = value.strip().replace("'", "")  # Eliminar comillas simples

# Convertir el diccionario a JSON y escribirlo en un archivo
final=(archivo[0:-4])
resultado=final + ".json"
with open(resultado, 'w') as f:
    json.dump(data, f, indent=4)

print("está listo tu archivo: " , resultado)

