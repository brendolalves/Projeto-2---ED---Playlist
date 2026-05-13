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
        opcao = exibir_menu

        if opcao == "1": 
            try:
                titulo = input("Titulo: ")
                artista = input("Artista: ")
                genero = input("Gênero: ")
                bpm = int(input("BPM: "))
                if bpm <= 0: raise ValueError
                bib.adicionar(titulo, artista, genero, bpm)
            except ValueError:
                print("Erro: BPM deve ser um número inteiro positivo.")
                

        elif opcao == "2":
            try:
                id_rem = int(input("ID para remover: "))
                if bib.remover(id_rem):
                    print("Removida com sucesso.")
                else:
                    print("Erro: ID inexistente.")
            except ValueError:
                print("Erro: ID inválido.")

        elif opcao == "3":
            termo = input("Digite o ID ou Título: ")
            resultado = bib.buscar(termo)
            if resultado:
                print(f"Encontrada: {resultado}")
            else:
                print("Música não encontrada.")

        elif opcao == "4": 
            print("\n--- BIBLIOTECA COMPLETA ---")
            atual = bib.inicio
            count = 0
            while atual:
                print(atual.musica)
                atual = atual.proximo
                count += 1
            if count == 0: print("Biblioteca vazia.")

        elif opcao == "5":
            montar_filas(bib, f_relaxar, f_focar, f_animar, f_treinar)
            print("Filas de humor atualizadas!") 

        elif opcao == "6": 
            print("1-Relaxar, 2-Focar, 3-Animar, 4-Treinar")
            h = input("Humor: ")
            selecionada = {"1": f_relaxar, "2": f_focar, "3": f_animar, "4": f_treinar}.get(h)

            if selecionada:
                musica = selecionada.dequeue()
                if musica:
                    print(f"Tocando agora: {musica}")
                    historico.enqueue(musica)
                else:
                    print("Erro: Fila de humor vazia.")
            else:
                print("Opção inválida.")

        elif opcao == "7":
            print("1-Relaxar, 2-Focar, 3-Animar, 4-Treinar")
            h = input("Humor: ")
            selecionada = {"1": f_relaxar, "2": f_focar, "3": f_animar, "4": f_treinar}.get(h)
            if selecionada:
                print(f"--- Fila Selecionada ---")
                selecionada.exibir_fila()
            else:
                print("Opção inválida.") 

        elif opcao == "8": 
            print("\n--- HISTÓRICO DE REPRODUÇÃO ---")
            historico.exibir_fila() 

        elif opcao == "9":
            total_bib = 0
            atual = bib.inicio
            while atual:
                total_bib += 1
                atual = atual.proximo
            print(f"\nTotal na Biblioteca: {total_bib}")
            print(f"Relaxar: {f_relaxar.total} | Focar: {f_focar.total}")
            print(f"Animar: {f_animar.total} | Treinar: {f_treinar.total}")
            print(f"Total Reproduzidas: {historico.total}") 

        elif opcao == "10":
            print("Encerrando sistema...")
            break

if __name__ == "__main__":
    main()

        
