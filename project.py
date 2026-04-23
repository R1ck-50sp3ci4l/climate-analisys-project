import random
import math
import matplotlib.pyplot as plt

def riempi_giorni():
    lista_temperatura=[]
    temperatura_iniziale=random.randint(-10,5)
    lista_temperatura.append(temperatura_iniziale)
    t=temperatura_iniziale
    for i in range(1,24):
        incremento=random.randint(0,3)
        if i>17:
            t=t-incremento
        else:
            t=t+incremento
        lista_temperatura.append(t)
    print(lista_temperatura)
    return(lista_temperatura)
    
    
   
def calcolo_media(lista_giorni):
    lista_medie=[]
    for i in range(7):
        somma=0
        lista_temperatura=lista_giorni[i]
        for j in range(24):
            somma=somma+lista_temperatura[j]
        media=somma/len(lista_temperatura)
        lista_medie.append(media)
    return(lista_medie)
    
    

def temperatura_minima(lista_giorni):
    lista_minima=[]
    for i in range(7):
        lista_temperatura=lista_giorni[i]
        for t in range(1,24):
            min=lista_temperatura[0]
            if lista_temperatura[t]<min:
                min=lista_temperatura[t]
        lista_minima.append(min)
    print("le temperature piu basse durante la settimana sono:")
    print(lista_minima)
            
            
def temperatura_massima(lista_giorni):
    lista_massima=[]
    for i in range(7):
        lista_temperatura=lista_giorni[i]
        for t in range(1,24):
            max=lista_temperatura[0]
            if lista_temperatura[t]>max:
                max=lista_temperatura[t]
        lista_massima.append(max)
    print("le temperature piu alte durante la settimana sono:")
    print(lista_massima)
            
def varianza(lista_medie, lista_giorni):
    lista_varianze = []
    for i in range(7):
        lista_calcoli = []  
        lista_temperatura = lista_giorni[i]
        for t in range(24):
            v = (lista_temperatura[t] - lista_medie[i])**2
            lista_calcoli.append(v)

        var = sum(lista_calcoli) / len(lista_calcoli)
        lista_varianze.append(var)

    return(lista_varianze)
  
    
def deviazione_standard(lista_varianze):
    lista_deviazione=[]
    for i in range(7):
        dev=math.sqrt(lista_varianze[i])
        lista_deviazione.append(dev)
    return(lista_deviazione)
        
def moda(lista_giorni):
     lista_moda=[]
     for  i in range(7):
        lista_temperatura=lista_giorni[i]
        moda=lista_temperatura[0]
        max_count=0
        for t in range(1,24):
            count=lista_temperatura.count(t)
            if count >max_count:
                max_count=count
                moda=t
        lista_moda.append(moda)
     print("la moda settimanale è:")
     print(lista_moda)
                
def crea_instogramma(dati ,num_bins=10 , titolo="instogramma", colore="skyblue"):
    plt.figure(figsize=(8, 5))
    plt.hist(dati, bins=num_bins, color=colore, edgecolor="black", alpha=0.7)
    plt.title(titolo)
    plt.xlabel("Valori")
    plt.ylabel("Frequenza")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def covarianza(lista_giorni,lista_medie):
    
    for i in range(7):
        if i==6:
            break
        t=i+1
        lista_temperatura=lista_giorni[i]
        lista_t=lista_giorni[t]
        lista_covarianza=[]
       
        for j in range(24):
            
            covarianza=(lista_temperatura[j]*lista_medie[i])*(lista_t[j]*lista_medie[i])/len(lista_temperatura)
            lista_covarianza.append(covarianza)
        print("le covarianze sono")
        print(lista_covarianza)



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
    


        
    