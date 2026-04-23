from project import *
import random
import math
import matplotlib.pyplot as plt
if __name__ == "__main__":
    print("temperature rilevate")        
    lista_giorni=[]
    for i in range(7):
        lista_giorni.append(riempi_giorni())

    lista_medie=calcolo_media(lista_giorni)
    print("le medie settimanali sono:")
    print(lista_medie)
    ris= varianza(lista_medie , lista_giorni)
    print("la varianza settimanale è:")
    print(ris)
    lista_varianze=varianza(lista_medie, lista_giorni)
    G=deviazione_standard(lista_varianze)
    print("la deviazione standard settimanale è:")
    print(G)
    moda(lista_giorni)
    covarianza(lista_giorni,lista_medie)


    temperatura_minima(lista_giorni)

    temperatura_massima(lista_giorni)
    
    varianza(lista_medie,lista_giorni)
    for i in range(7):
        lista_temperatura=lista_giorni[i]
        crea_instogramma(lista_temperatura ,num_bins=10 , titolo="instogramma", colore="skyblue")
    


        
    
            