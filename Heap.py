class heap:
    def __init__(self):

        self.lista = []  # dichiarata la lista che conterrà tutti i valori di heap
        self.heapSize = 0

    # aggiunge il valore senza ordinare
    def add(self, valore):
        self.lista.append(valore)
        self.heapSize += 1

    def swap(self, fpos, spos):

        self.lista[fpos], self.lista[spos] = (self.lista[spos], self.lista[fpos])

    def inserisci_elemento(self, valore):

        self.lista.append(valore)
        self.heapSize += 1
        self.max_heapify_up(self.heapSize - 1)

    def left(self, i):

        return 2 * i + 1

    def right(self, i):

        return 2 * i + 2

    def parent(self, i):

        return i // 2

    def max_heapify_up(self, index):  # i è il valore della radix attuale a cui stiamo applicando la nostra funzione

        while index > 0:
            parent_index = (index - 1) // 2
            if self.lista[index] > self.lista[parent_index]:
                # Swap the current element with its parent
                self.lista[index], self.lista[parent_index] = self.lista[parent_index], self.lista[index]
                index = parent_index
            else:
                break

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left <= self.heapSize -1:
            if self.lista[left] > self.lista[i]:
                largest = left


        if right <= self.heapSize -1:
            if self.lista[right] > self.lista[i]:
                largest = right

        if largest != i:
            self.lista[i], self.lista[largest] = self.lista[largest], self.lista[i]
            self.max_heapify(largest)

    def build_max_heap(self):

        self.heapSize = len(self.lista)  # qua heapSize acquisisce un valore

        for i in range((len(self.lista)-1) // 2, -1, -1):
            self.max_heapify(i)


    def heap_maximum(self):
        if self.heapSize >= 1:
            return self.lista[0]  # ritorna il primo elemento della lista

        else:
            return None  # Restituisci None se l'heap è vuoto


    def aggiorna_elemento(self, indice, nuovo_valore):
        if 0 <= indice < self.heapSize:
            self.lista[indice] = nuovo_valore
            self.max_heapify(indice)

    def rimuovi_elemento(self, indice):
        if 0 <= indice < self.heapSize:
            # Sostituisci l'elemento da rimuovere con l'ultimo elemento
            self.lista[indice] = self.lista[self.heapSize - 1]
            self.lista.remove(self.lista[self.heapSize - 1])
            self.heapSize -= 1
            self.max_heapify(indice - 1)  # sufficiente max_heapify poichè aggiusto solo il sottoalbero
