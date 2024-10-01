import time
usuario = str (input("Ingresa tu nombre por favor:")).capitalize()
global puntos
puntos = 0

print(f"Hola {usuario} a partir de ahora te voy a mostrar una serie de palabras\ny vas a responder con un anagrama.")

lista_anag = ["saco", "fresa", "algo", "sopa", "toro", "pata", "aries", "blanco", "barco", "monja"]
anagramas_existentes = ["asco", "caos", "caso", "cosa", "ocas", "soca","fares", "frase", "rafes","lago", "goal", "gola",
                        "sapo", "paso", "roto", "orto", "tapa", "apta", "balcon", "braco", "cobra", "broca", "jamon"]

for anag in lista_anag:
    
    rta = str(input(f"Anagrama de {anag}:"))
    rta1 = rta.lower()
    if rta1 == anag:
        print("No vale usar la misma palabra como anagrama.")
    elif rta1 not in anagramas_existentes:
        print("Eso no es una palabra!!!")
    
    else:
        if rta1 != anag:            
            rta_lst = list(rta1)    
            rta_lst.sort()
            palabra = list(anag)
            palabra.sort()
            if rta_lst == palabra:
                print(f"Bien ahi {usuario}, ganaste un punto.")
                puntos += 1
                print(f"Llevas {puntos} punto.")
            else:
                print(f"Noup, seguis teniendo {puntos} puntos.")
        else:
            print("No vale usar la misma palabra. No sumas puntos.")

if puntos <= 3:
    print(f"Hiciste {puntos} puntos... A seguir practicando, vos podes.")
if puntos > 3 and puntos < 7:
    print(f"Hiciste {puntos} puntos... Es un buen puntaje.")
if puntos >= 7 and puntos <= 9:
    print(f"Muy bien che... {puntos} puntos!!!")
if puntos == 10:
    print("Puntaje perfecto.")
