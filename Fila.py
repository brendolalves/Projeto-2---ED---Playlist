from Musica import NodaFila

class Fila:
    def __init__(self):
        self.frente = None
        self.fim = None
        self.total = 0

def enqueue(self, musica):
    novo_nodo = NodaFila(musica)
    if self.fim is None:
        self.frente = self.fim = novo_nodo
    else:
        self.fim.proximo = novo_nodo
        self.fim = novo_nodo
    self.total += 1

def dequeue(self):
    if self.frente is None:
        return None
    removido = self.frente.musica
    self.frente = self.frente.proximo
    if self.frente is None:
        self.fim = None
    self.total -= 1
    return removido


    