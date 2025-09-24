from dataclasses import dataclass
from datetime import datetime

# Define uma estrutura de dados para representar uma publicação
@dataclass 
class Publicacao:
    conteudo: str
    descricao: str 
    autor: str
    data_hora: datetime
    curtidas: int = 0  # Começa com 0 curtidas

# Lista onde todas as publicações serão armazenadas
lista_publicacoes = []

# Função para criar uma nova publicação
def criar_publicacao():
    print("\n=== CRIAR PUBLICAÇÃO ===")
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Digite a descrição: ")
    autor = input("Digite o nome do autor: ")
    data_hora = datetime.now()  # Pega a data e hora atual

    # Cria uma nova publicação com os dados fornecidos
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)  # Adiciona na lista
    print("Publicação criada com sucesso!")

# Função para mostrar o feed com todas as publicações resumidas
def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    # Mostra cada publicação com número, autor, curtidas, trecho do conteúdo e data
    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"{i}. {pub.autor} - {pub.curtidas} curtidas")
        print(f"    {pub.conteudo[:50]}...")  # Mostra apenas os 50 primeiros caracteres
        print(f"    {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)

# Função para curtir uma publicação escolhida pelo número
def curtir_publicacao():
    print("\n=== CURTIR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return 

    visualizar_feed()  # Mostra as publicações disponíveis
    try:
        # Pede o número da publicação a ser curtida
        indice = int(input("Digite o número da publicação para curtir: ")) - 1 
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1  # Adiciona uma curtida
            print("Publicação curtida!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

# Função para mostrar todos os detalhes de uma única publicação
def visualizar_publicacao_individual():
    print("\n=== VISUALIZAR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    visualizar_feed()  # Mostra o feed para o usuário escolher a publicação
    try:
        indice = int(input("Digite o número da publicação: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            # Exibe todos os detalhes da publicação escolhida
            print(f"\nAutor: {pub.autor}")
            print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"Conteúdo: {pub.conteudo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

# Função para ver publicações feitas por um autor específico
def visualizar_publicacoes_por_autor():
    print("\n=== PUBLICAÇÕES POR AUTOR ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return

    autor = input("Digite o nome do autor: ")
    # Filtra as publicações que têm o mesmo nome de autor (sem diferenciar maiúsculas)
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]

    if not publicacoes_autor:
        print(f"Nenhuma publicação encontrada para {autor}.")
        return

    # Exibe todas as publicações do autor encontrado
    print(f"\nPublicações de {autor}:")
    for pub in publicacoes_autor:
        print(f"- {pub.conteudo[:50]}... ({pub.curtidas} curtidas)")
        print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 30)

# Menu principal que mostra as opções e executa as funções
def menu():
    while True:
        print("\n=== REDE SOCIAL ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Visualizar Feed")
        print("4. Visualizar Publicação Individual")
        print("5. Visualizar Publicações por Autor")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        # Verifica qual opção o usuário escolheu e chama a função correspondente
        if opcao == "1":
            criar_publicacao()
        elif opcao == "2":
            curtir_publicacao()
        elif opcao == "3":
            visualizar_feed()
        elif opcao == "4":
            visualizar_publicacao_individual()
        elif opcao == "5":
            visualizar_publicacoes_por_autor()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Inicia o programa chamando o menu
if __name__ == "__main__":
    menu()
