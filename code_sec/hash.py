import hashlib
import webbrowser

def generar_hashes(palabra):
    return {
        "MD5": hashlib.md5(palabra.encode()).hexdigest(),
        "SHA-1": hashlib.sha1(palabra.encode()).hexdigest(),
        "SHA-256": hashlib.sha256(palabra.encode()).hexdigest()
    }

# Hashes predefinidos de palabras originales
hashes_predefinidos = {
    "MD5": "040342c014ffc1c11592948bd92e3721",
    "SHA-1": "410013f679f8a5f0c2995c0432467124ef7cea10",
    "SHA-256": "67b6a6b3785f0ce05f692e11e84c4c6196872760cd247c3ce2e66dd008381d19"
}

# Pedir la palabra al usuario sin mostrar su hash
palabra_ingresada = input("Ingresa una palabra para comparar: ")
hashes_ingresados = generar_hashes(palabra_ingresada)

# Comparación sin mostrar los hashes
coincidencia = False

for algoritmo, hash_predefinido in hashes_predefinidos.items():
    if hashes_ingresados[algoritmo] == hash_predefinido:
        print(f"La palabra ingresada coincide con un hash almacenado en {algoritmo}.")
        print("Abriendo enlace...")
        webbrowser.open("https://github.com/")
        coincidencia = True
        break

if not coincidencia:
    print("La palabra ingresada no coincide con ningún hash almacenado.")