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

