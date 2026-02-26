codigo_de_identificacion = input("ingresa la identificacion del libro:").strip()

if not codigo_de_identificacion.startswith("LIB-"):
    if "-" in codigo_de_identificacion:
        codigo_de_identificacion = codigo_de_identificacion.split("-",1)[1]
        codigo_de_identificacion = "LIB-" + codigo_de_identificacion

        codigo_parte_numerica = codigo_de_identificacion[4:]

        if len(codigo_parte_numerica) == 10 or len(codigo_parte_numerica) == 13:
            print("codigo correcto:", codigo_de_identificacion)
        else:
            print("codigo invalido. La parte numerica debe tener 10 o 13 caracteres.")