from Fila import Fila
from Biblioteca import Biblioteca
from humor import montar_filas

def exibir_menu():
    print("\n" + "="*30)
    print("--Playlist--")
    print("="*30)
    print("1. Adcionar música")
    print("2. Remover música")
    print("3. Buscar música")
    print("4. Listar biblioteca")
    print("5. Montar filas por humor")
    print("6. Reproduzir próxima (Pular)")
    print("7. Exibir fila de humor")
    print("8. Exibir histórico")
    print("9. Estatística")
    print("10. Sair")
    return input("Escolha uma opção: ")

def main():
    bib = Biblioteca()
    f_relaxar = Fila()
    f_focar = Fila()
    f_animar = Fila()
    f_treinar = Fila()
    historico = Fila()

    while True:
        opçao = exibir_menu

        if opçao == "1": 
            try:
                titulo = input("Titulo: ")
                artista = input("Artista: ")
                genero = input("Gênero: ")
                bpm = int(input("BPM: "))
                if bpm <= 0: raise ValueError
                bib.adicionar(titulo, artista, genero, bpm)
            except ValueError:
                print("Erro: BPM deve ser um número inteiro positivo.")


