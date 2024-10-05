traduccion= {
    "JUICIOSO":"persona responsable que cumple los deberes",
    "CANGUIL":"maiz pira o palomita de maiz",
    "AGUACATE":"es una fruta conocida como palta"
}

palabra=input("ingresa una palabra en mayusculas")

if palabra in traduccion.keys():
    print("su significado es :", traduccion[palabra])
else:
    print("la palabra no existe")
