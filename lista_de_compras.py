import os
import random

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função p/ definir a unidade de medida.
def unidade_medida():
    while True:
        print('A. QUILOGRAMA')
        print('B. GRAMA')
        print('C. LITRO')
        print('D. MILILITRO')
        print('E. UNIDADE')
        print('F. METRO')
        print('G. CENTÍMETRO')
        escolha = input('Qual a unidade de medida do produto? ').upper()

        dicionario_unidades = {'A': 'kg', 'B': 'g', 'C': 'l', 'D': 'ml', 'E': 'und', 'F': 'm', 'G': 'cm'}

        if escolha in dicionario_unidades:
            unidade_final = dicionario_unidades[escolha]
            return unidade_final

        else:
            print('\n❌ Opção de unidade inválida! Tente novamente.')
            continue

#Função p/ definir a quantidade.
def quantidade():
    while True:
        qtd = input('Qual a quantidade estocada? ')

        if qtd.isdigit():  # Verifica se o texto contém apenas números
            return int(qtd)
        else:
            print('❌ Erro: Por favor, digite apenas números!')
        continue

#Função p/ adicionar produto a lista.
def adicionar_produto(lista): #Tudo que for adicionado a (lista) sera direcionado para (lista_produtos).
    produto = input('Qual o nome do produto? ').upper()
    id = random.randint(10000, 99999)
    unidade_final = unidade_medida()
    qtd = quantidade()
    desc = input('Adicione uma descrição ao produto: ')
    lista.append([produto, id, unidade_final, qtd, desc])
    limpar_terminal()
    print(f'✅ {produto} (ID: {id}) adicionado!')
    print('')

#Função p/ remover produto da lista
def remover_produto(lista):
    while True:
        busca_id = input('Qual a ID do produto que deseja remover? ')
        if busca_id.isdigit():
            busca_id = int(busca_id)
        else:
            print('❌ Erro: Por favor, digite apenas números!')
            continue

        encontrado = False
        #Percorre a lista para encontrar o ID
        for i in range(len(lista)):
            if lista[i][1] == busca_id: #[i] percorre todos os valores da posição [1] da lista (ID)
                nome_removido = lista[i][0] #Mesma utilidade, posição [0] se encontra o nome do produto
                lista.pop(i)  #Remove o item e suas info. da lista
                limpar_terminal()
                print(f'✅ Produto "{nome_removido}" (ID: {busca_id}) removido com sucesso!')
                encontrado = True
                break

        if encontrado:
            break  # Sai do 'while' e volta para o menu
        else:
            print(f'⚠️ Produto com ID {busca_id} não encontrado!')

            while True:

                opcao = input('Deseja tentar outro ID? (S/N): ').upper()
                if opcao == 'S':
                    break
                elif opcao == 'N':
                    limpar_terminal()
                    return
                else:
                    print('❌ Opção invalida, tente novamente digitando S ou N!')
                    continue

#Função p/ definir a procura de produtos
def procurar_produto(lista):
    while True:
        pesquisa = input('Qual produto deseja encontrar? ').upper()

        itens_encontrados = []

        for produto in lista:
            if pesquisa in produto[0]:
                itens_encontrados.append(produto)

        limpar_terminal()

        quantidade_achada = len(itens_encontrados)

        if quantidade_achada > 0:
            print(f'✅ {quantidade_achada} item(ns) encontrado(s)!\n')

            for item in itens_encontrados:
                nome, id_prod, und, qtd, desc = item  # Desempacotando a lista
                print(f'{nome} ({id_prod}) \nUnidade: {und} \nQtd: {qtd} \nDescrição: {desc}\n')

            while True:
                opcao = input('Deseja procurar outro produto? (S/N): ').upper()
                if opcao == 'S':
                    limpar_terminal()
                    break
                elif opcao == 'N':
                    limpar_terminal()
                    return
                else:
                    print('❌ Opção inválida! Digite S ou N.')

        else:
            print(f'❌ Nenhum produto encontrado com o termo "{pesquisa}" ❌')
            while True:
                opcao = input('\nDeseja tentar outra pesquisa? (S/N): ').upper()
                if opcao == 'S':
                    limpar_terminal()
                    break
                elif opcao == 'N':
                    return
                else:
                    print('❌ Opção inválida! Digite S ou N.')

#Cabeçalho.
print('')
print('Olá!')
print('Esta é uma lista de compras simples e interativa')

def menu_principal():
    while True:
        num = 0
        print('--------------------------------------')
        print('-- LISTA DE PRODUTOS --')
        if not lista_produtos:
            print('\n (LISTA VAZIA)')

        #Rodar todos itens da lista.
        for produto in lista_produtos:

            num = num + 1
            nome = produto[0]
            id = produto[1]
            und = produto[2]
            qtd = produto[3]
            desc = produto[4]

            print(f' \n{num}. {nome} ({id}) \nUnidade de medida: {und} \nQuantidade: {qtd} \nDescrição: {desc}')
        print('')
        print('--------------------------------------')
        print('A. ADICIONAR PRODUTO')
        print('B. REMOVER PRODUTO')
        print('C. PESQUISAR PRODUTO')
        print('D. SAIR DO PROGRAMA')
        opcao = input('O que deseja realizar? ').upper()

        if opcao == 'D':
            print('Obrigado por utilizar a lista de compras!')
            break

        if opcao not in ('A', 'B', 'C', 'D'):
            limpar_terminal()
            print ('==================Opção invalida, tente novamente!==================')
            print('')
            continue

        if opcao == 'A':
            adicionar_produto(lista_produtos)

        if opcao == 'B':
            remover_produto(lista_produtos)

        if opcao == 'C':
            procurar_produto(lista_produtos)

lista_produtos = []
menu_principal()