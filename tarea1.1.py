
nombre = input ("Ingrese el nombre de la categoria: ").strip()
if 5 <= len(nombre) <=12:
    nombre_mayus = nombre.upper()
    print(f"categoria registrada exitosamente: {nombre_mayus}") 
else:
    print("la categoria que ingresaste no cumple con su requerimiento")