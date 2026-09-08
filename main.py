#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_logo():
    """Exibe o logo do sistema"""
    print("""
    ╔══════════════════════════════════════════╗
    ║         SABORES EXPRESS                  ║
    ║      Sistema de Gestão de Restaurantes   ║
    ╚══════════════════════════════════════════╝
    """)

def carregar_dados_json():
    """Carrega dados dos arquivos JSON para o sistema"""
    arquivos_json = [
        'Burger King.json',
        'KFC.json',
        'McDonald’s.json',
        'Pizza Hut.json',
        'Taco Bell.json',
        'Wendy’s.json'
    ]
    
    restaurantes_carregados = []
    
    for arquivo in arquivos_json:
        if os.path.exists(arquivo):
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    nome_restaurante = arquivo.replace('.json', '')
                    
                    # Criar restaurante
                    restaurante = Restaurante(nome_restaurante, "Fast Food")
                    restaurante._ativo = True
                    
                    # Adicionar itens ao cardápio (max 5 por restaurante)
                    for item in dados[:5]:
                        nome_item = item['item']
                        preco = item['price']
                        descricao = item['description']
                        
                        # Detecta se é bebida por palavras-chave
                        bebidas_keywords = ['drink', 'soda', 'tea', 'coffee', 'milk', 
                                          'shake', 'freeze', 'juice', 'water', 'cola',
                                          'pepsi', 'dew', 'sprite', 'lemonade']
                        
                        is_bebida = any(keyword in nome_item.lower() for keyword in bebidas_keywords)
                        
                        if is_bebida:
                            tamanho = "Médio"
                            if 'small' in nome_item.lower() or '12 fl' in nome_item.lower():
                                tamanho = "Pequeno"
                            elif 'large' in nome_item.lower() or '30 fl' in nome_item.lower() or '38 fl' in nome_item.lower():
                                tamanho = "Grande"
                            elif 'medium' in nome_item.lower() or '20 fl' in nome_item.lower():
                                tamanho = "Médio"
                            
                            bebida = Bebida(nome_item, preco, tamanho)
                            restaurante.adicionar_no_cardapio(bebida)
                        else:
                            prato = Prato(nome_item, preco, descricao)
                            restaurante.adicionar_no_cardapio(prato)
                    
                    restaurantes_carregados.append(restaurante)
                    print(f"✅ {nome_restaurante} carregado com sucesso!")
                    
            except Exception as e:
                print(f"❌ Erro ao carregar {arquivo}: {e}")
        else:
            print(f"⚠️  Arquivo {arquivo} não encontrado")
    
    return restaurantes_carregados

def menu_principal():
    """Exibe o menu principal"""
    print("""
    ╔══════════════════════════════════════════╗
    ║           MENU PRINCIPAL                 ║
    ╠══════════════════════════════════════════╣
    ║  1. 📋 Listar Restaurantes               ║
    ║  2. ➕ Cadastrar Novo Restaurante        ║
    ║  3. 🔄 Alternar Estado do Restaurante    ║
    ║  4. ⭐ Avaliar Restaurante               ║
    ║  5. 🍽️ Ver Cardápio                      ║
    ║  6. 🍔 Adicionar Item ao Cardápio        ║
    ║  0. 🚪 Sair                              ║
    ╚══════════════════════════════════════════╝
    """)

def cadastrar_restaurante():
    """Cadastra um novo restaurante"""
    print("\n--- CADASTRO DE RESTAURANTE ---")
    nome = input("Nome do restaurante: ")
    
    categoria = input("Categoria: ")
    
    restaurante = Restaurante(nome, categoria)
    print(f"\n✅ Restaurante '{nome}' cadastrado com sucesso!")
    return restaurante

def alternar_estado():
    """Alterna o estado (ativo/inativo) de um restaurante"""
    if not Restaurante.restaurantes:
        print("\n❌ Nenhum restaurante cadastrado!")
        return
    
    print("\n--- RESTAURANTES DISPONÍVEIS ---")
    for i, restaurante in enumerate(Restaurante.restaurantes, 1):
        status = "Ativo" if restaurante._ativo else "Inativo"
        print(f"{i}. {restaurante._nome} [{status}]")
    
    try:
        opcao = int(input("\nEscolha o número do restaurante: ")) - 1
        if 0 <= opcao < len(Restaurante.restaurantes):
            restaurante = Restaurante.restaurantes[opcao]
            restaurante.alternar_estado()
            estado = "ativado" if restaurante._ativo else "desativado"
            print(f"\n✅ Restaurante '{restaurante._nome}' {estado}!")
        else:
            print("\n❌ Opção inválida!")
    except ValueError:
        print("\n❌ Por favor, digite um número!")

def avaliar_restaurante():
    """Adiciona uma avaliação a um restaurante"""
    if not Restaurante.restaurantes:
        print("\n❌ Nenhum restaurante cadastrado!")
        return
    
    print("\n--- AVALIAR RESTAURANTE ---")
    for i, restaurante in enumerate(Restaurante.restaurantes, 1):
        print(f"{i}. {restaurante._nome}")
    
    try:
        opcao = int(input("\nEscolha o número do restaurante: ")) - 1
        if 0 <= opcao < len(Restaurante.restaurantes):
            restaurante = Restaurante.restaurantes[opcao]
            cliente = input("Seu nome: ")
            nota = float(input("Nota (1-5): "))
            
            if 0 < nota <= 5:
                restaurante.receber_avaliacao(cliente, nota)
                print(f"\n✅ Avaliação registrada! Média atual: {restaurante.media_avaliacoes}")
            else:
                print("\n❌ Nota deve ser entre 1 e 5!")
        else:
            print("\n❌ Opção inválida!")
    except ValueError:
        print("\n❌ Por favor, digite valores válidos!")

def ver_cardapio():
    """Exibe o cardápio de um restaurante"""
    if not Restaurante.restaurantes:
        print("\n❌ Nenhum restaurante cadastrado!")
        return
    
    print("\n--- SELECIONE O RESTAURANTE ---")
    for i, restaurante in enumerate(Restaurante.restaurantes, 1):
        print(f"{i}. {restaurante._nome}")
    
    try:
        opcao = int(input("\nEscolha o número: ")) - 1
        if 0 <= opcao < len(Restaurante.restaurantes):
            Restaurante.restaurantes[opcao].exibir_cardapio()
        else:
            print("\n❌ Opção inválida!")
    except ValueError:
        print("\n❌ Por favor, digite um número!")

def adicionar_item_cardapio():
    """Adiciona um item ao cardápio"""
    if not Restaurante.restaurantes:
        print("\n❌ Nenhum restaurante cadastrado!")
        return
    
    print("\n--- ADICIONAR ITEM AO CARDÁPIO ---")
    for i, restaurante in enumerate(Restaurante.restaurantes, 1):
        print(f"{i}. {restaurante._nome}")
    
    try:
        opcao = int(input("\nEscolha o restaurante: ")) - 1
        if 0 <= opcao < len(Restaurante.restaurantes):
            restaurante = Restaurante.restaurantes[opcao]
            
            print("\nTipo de item:")
            print("1. 🍽️  Prato")
            print("2. 🥤 Bebida")
            tipo = input("Escolha: ")
            
            nome = input("Nome do item: ")
            preco = float(input("Preço: R$ "))
            
            if tipo == "1":
                descricao = input("Descrição: ")
                item = Prato(nome, preco, descricao)
            elif tipo == "2":
                tamanho = input("Tamanho (Pequeno/Médio/Grande): ")
                item = Bebida(nome, preco, tamanho)
            else:
                print("\n❌ Tipo inválido!")
                return
            
            restaurante.adicionar_no_cardapio(item)
            print(f"\n✅ '{nome}' adicionado ao cardápio!")
        else:
            print("\n❌ Opção inválida!")
    except ValueError:
        print("\n❌ Por favor, digite valores válidos!")

def main():
    """Função principal"""
    limpar_tela()
    exibir_logo()
    
    print("🔄 Carregando dados dos restaurantes...")
    carregar_dados_json()
    input("\nPressione ENTER para continuar...")
    
    while True:
        limpar_tela()
        exibir_logo()
        menu_principal()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            limpar_tela()
            print("\n--- LISTA DE RESTAURANTES ---")
            Restaurante.listar_restaurantes()
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "2":
            limpar_tela()
            cadastrar_restaurante()
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "3":
            limpar_tela()
            alternar_estado()
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "4":
            limpar_tela()
            avaliar_restaurante()
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "5":
            limpar_tela()
            ver_cardapio()
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "6":
            limpar_tela()
            adicionar_item_cardapio()
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "0":
            print("\n👋 Obrigado por usar o Sabores Express!")
            break
        else:
            print("\n❌ Opção inválida!")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()
