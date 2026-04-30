# Sistema de Playlist 
Este repositório contém o desenvolvimento do backend de um aplicativo de músicas, com foco na implementação manual de estruturas de dados lineares.\
O projeto foi desenvolvido como parte da disciplina de Estrutura de Dados da Fatec Rio Claro. 

##  Objetivo do Projeto:
O sistema permite que o usuário gerencie uma biblioteca pessoal de faixas, organize filas de reprodução baseadas no humor (através do BPM) e consulte um histórico de reproduções. \
O diferencial técnico é o uso exclusivo de **Listas Encadeadas** e **Filas FIFO** implementadas manualmente, sem o uso de estruturas nativas do Python como `list` ou `deque`. 

## Especificações Técnicas:
As seguintes classes compõem a arquitetura do sistema:
* Classe Musica: Representa uma faixa com ID, título, artista, gênero e BPM.
* Classe NodoLista: Nó para a lista encadeada simples da biblioteca.
* Classe Biblioteca: Lista encadeada para armazenamento e gestão (inserção, remoção e busca).
* Classe NodoFila: Nó para a implementação interna das filas.
* Classe Fila: Implementação manual de fila FIFO com as operações enqueue e dequeue.

## Funcionalidades:
O menu principal do sistema oferece as seguintes operações:
* Adicionar música: Cadastro com geração de ID sequencial.
* Remover música: Busca e remoção por ID na lista encadeada.
* Buscar música: Localização por ID ou título.
* Listar biblioteca: Exibição de todas as faixas cadastradas.
* Montar filas por humor: Distribuição automática baseada no BPM:

| Fila  | Genero  | BPM  |
| ----------- | ----------- | ----------- |
| Relaxar    | Tranquilo      | até 80      |
| Focar      | Concentração      | 81 à 120      |
| Animar      | Agitado      | 121 a 160      |
| Treinar      | Intenso      | acima de 160      |

Reproduzir próxima: Realiza o dequeue da fila de humor e move a música para o histórico.\
Exibir histórico: Lista todas as músicas já reproduzidas através de uma instância dedicada da classe Fila.\
Estatísticas: Exibe totais da biblioteca, tamanhos das filas e total reproduzido.

## Requisitos e Restrições

Não é permitido o uso de estruturas prontas (built-in) do Python para a lógica de dados.\
A cada nova montagem das filas de humor, as anteriores devem ser limpas.\
IDs não podem ser reutilizados após a remoção de uma música.\
O sistema trata entradas inválidas (BPM não numérico, IDs inexistentes, etc.).

## Cronograma e Avaliação

Entrega Final: Início da aula do dia 30/04/2026.\
Apresentação: 14/04/2026.\
Critérios: Serão avaliados a análise do código, o uso correto das estruturas de dados e a qualidade da apresentação.\

--- **Fatec Rio Claro - Segundo Projeto de Estrutura de Dados** 

