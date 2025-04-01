import hashlib

def generar_hash():
    palabra = input("Ingresa una palabra: ")
    
    hash_md5 = hashlib.md5(palabra.encode()).hexdigest()
    hash_sha1 = hashlib.sha1(palabra.encode()).hexdigest()
    hash_sha256 = hashlib.sha256(palabra.encode()).hexdigest()

    print("\nHashes generados:")
    print(f"MD5:     {hash_md5}")
    print(f"SHA-1:   {hash_sha1}")
    print(f"SHA-256: {hash_sha256}")

generar_hash()