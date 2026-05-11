class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return f"[ID: {self.id}] {self.titulo} - {self.artista} ({self.genero}) - BPM: {self.bpm}"
    
class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class NodaFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None