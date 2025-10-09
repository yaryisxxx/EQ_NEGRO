import random

def saludar(nombre):
    return f"Hola {nombre}, este es un ejemplo de función en Python."

def multiplicar(numero):
    return numero * 2

def mensaje_motivacional():
    mensajes = [
        "¡Sigue adelante, lo estás haciendo muy bien!",
        "Cada error te acerca más al éxito.",
        "Nunca dejes de aprender cosas nuevas.",
        "El esfuerzo constante trae buenos resultados."
    ]
    return random.choice(mensajes)

if __name__ == "__main__":
    print(saludar("Equipo Negro"))

numero = 10
resultado = multiplicar(numero)
print(f"El doble de {numero} es {resultado}")

def dato():
    datos = [
        "Los pulpos tienen tres corazones.",
        "En Python, todo es un objeto, ¡incluso los números!",
        "Las abejas pueden reconocer rostros humanos.",
        "El ADN humano y el del plátano comparten un 50% de similitud.",
        "El símbolo ‘@’ se llama arroba por su forma en espiral."
    ]
    return random.choice(datos)

print(f"Dato curioso: {dato()}")
print(f"Mensaje del día: {mensaje_motivacional()}")
