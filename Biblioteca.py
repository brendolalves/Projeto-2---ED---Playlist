from Musica import Musica, NodoLista

class Biblioteca:
    def __init__(self):
        self.inicio = None
        self.contador_id = 1

    def adicionar(self, titulo, artista, genero, bpm):
        nova_musica = Musica(self.contador_id, titulo, artista, genero, bpm)
        novo_nodo = NodoLista(nova_musica)
        self.contador_id += 1

        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def remover(self, id_alvo):
        atual = self.inicio
        anterior = None
        while atual:
            if atual.musica.id == id_alvo:
                if anterior:
                    anterior.proximo = anterior.proximo
                else:
                    self.inicio = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar(self, termo):
        atual = self.inicio
        while atual:
            if str(atual.musica_id) == str(termo) or atual.musica.titulo.lower() == str(termo).lower():
                return atual.musica
            atual = atual.proximo
        return None