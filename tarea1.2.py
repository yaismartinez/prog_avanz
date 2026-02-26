opinion_usuario = input("Ingrese la opinion sobre el libro:")
opinion_sin_espacios = opinion_usuario.strip()
opinion_sin_espacios = opinion_sin_espacios.lower()
palabras_clave = opinion_sin_espacios.split()
contador = palabras_clave.count("recomiendo")

print("opinion procesada:")
print(opinion_sin_espacios)
print("la palabra clave 'recomiendo' aparece", contador, "veces")