import os
import timeit
from time import perf_counter as ptimer
from timeit import default_timer as timer
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import ListaConcatenata

matplotlib.use('TkAgg')
import random
import Heap


# voglio provare a modificare lo scorso programma con una variabile aggiuntiva: provare a misurare n inserimenti e non solo uno, per avere un tempo maggiore


def testListaConcatenata(dimMax, n, passo,numripetizioniinterne):  # n corrisponde al numero di ripetizioni
    lista = ListaConcatenata.Listaconcatenata()
    tempi_di_inserimento_lista_totali = []
    tempi_di_ricerca_massimo_lista_totali = []
    media_inserimento = []
    media_ricercamax = []
    # eseguo i test completi n volte
    for i in range(n):
        iteratore = 0
        for j in range(0, dimMax, passo):  # il passo identifica quanto voglio ingrandire via via la mia struttura dati

            t_tot = 0
            t_tot_media = 0

            # popolo a caso la mia lista, cosi ho una struttura che aumenta la sua grandezza ad ogni iterazione.

            for k in range(passo):
                dato = random.randint(0, dimMax)

                start_time = ptimer()
                for _ in range(numripetizioniinterne):
                    lista.aggiungi_elemento(dato)
                end_time = ptimer()

                t_tot += (end_time - start_time) / 10
                if numripetizioniinterne > 1:
                    for _ in range(numripetizioniinterne - 1):
                        lista.cancella_in_testa()  # tolgo tutti gli elementi eccetto che uno per far si che trova il massimo si può basare su una struttura dati

            t_medio = t_tot / passo  # divido il tempo totale per il numero di elementi che ho aggiunto cosi da averne una media

            start_time1 = ptimer()
            for _ in range(numripetizioniinterne):
                lista.trova_massimo()
            end_time1 = ptimer()
            t_tot_media = (end_time1 - start_time1) / 10  # media totale delle ricerche

            # tempi_di_ricerca_massimo_lista[(j-1) // passo]=
            if i == 0:
                tempi_di_inserimento_lista_totali.append(t_medio)
                tempi_di_ricerca_massimo_lista_totali.append(t_tot_media)

            else:
                tempi_di_inserimento_lista_totali[iteratore] += t_medio
                tempi_di_ricerca_massimo_lista_totali[iteratore] += t_tot_media
            iteratore += 1
            # tempi_di_ricerca_massimo_lista.append(end_time1-start_time1)  # salvo il valore del tempo impiegato per trovare il max
        # tempi_di_inserimento_lista_totali.append(t_medio)
        # tempi_di_ricerca_massimo_lista_totali.append(end_time1 - start_time1)

    for l in range(len(tempi_di_inserimento_lista_totali)):
        media = tempi_di_inserimento_lista_totali[l] / n
        media_inserimento.append(media)

    for l in range(len(tempi_di_ricerca_massimo_lista_totali)):
        media = tempi_di_ricerca_massimo_lista_totali[l] / n
        media_ricercamax.append(media)

    asse_x = [i for i in range(0, dimMax, passo)]
    plt.plot(asse_x, media_inserimento, label="insert", color="green")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento')
    plt.grid(True)
    plt.legend()
    plt.show()

    asse_x1 = [i for i in range(0, dimMax, passo)]
    plt.plot(asse_x1, media_ricercamax, label="Ricerca Max", color="orange")
    plt.xlabel('Numero elementi')
    plt.ylabel('tempo ricerca')
    plt.title('Tempo di ricerca di un max')
    plt.grid(True)
    plt.legend()
    plt.show()


testListaConcatenata(dimMax=1000, n=15, passo=10,numripetizioniinterne=150)
