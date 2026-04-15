# 🍽️ Sabores Express — Sistema de Gestão de Restaurantes

> Aplicação CLI em Python para gerenciamento de restaurantes, cardápios e avaliações, com carregamento de dados via JSON e estrutura orientada a objetos.

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Paradigm](https://img.shields.io/badge/Paradigma-POO-blueviolet?style=flat-square)
![Type](https://img.shields.io/badge/Tipo-CLI-gray?style=flat-square)

---

## 📋 Sobre o Projeto

**Sabores Express** é um sistema de gerenciamento de restaurantes desenvolvido em Python com foco em **Programação Orientada a Objetos (POO)**. A aplicação roda via terminal e permite cadastrar restaurantes, gerenciar cardápios com pratos e bebidas, registrar avaliações de clientes e calcular médias automaticamente.

Os dados de restaurantes reais (Burger King, McDonald's, KFC, Pizza Hut, Taco Bell e Wendy's) são carregados a partir de arquivos **JSON**, demonstrando integração com leitura e parsing de dados externos.

---

## ✨ Funcionalidades

- ✅ Listar restaurantes com nome, categoria, avaliação média e status
- ✅ Cadastrar novos restaurantes com nome e categoria
- ✅ Alternar status do restaurante entre **Ativo** e **Inativo**
- ✅ Avaliar restaurantes com nota de 1 a 5 e cálculo automático de média
- ✅ Visualizar cardápio completo por restaurante
- ✅ Adicionar itens ao cardápio como **Prato** (com descrição) ou **Bebida** (com tamanho)
- ✅ Carregamento automático de dados reais via arquivos JSON

---

## 🏗️ Estrutura do Projeto

```
restaurante/
├── main.py                  # Ponto de entrada e menu principal
├── requirements.txt         # Dependências
├── modelos/
│   ├── restaurante.py       # Classe Restaurante
│   ├── avaliacao.py         # Classe Avaliacao
│   └── cardapio/
│       ├── item_cardapio.py # Classe base ItemCardapio
│       ├── prato.py         # Classe Prato (herda ItemCardapio)
│       └── bebida.py        # Classe Bebida (herda ItemCardapio)
├── Burger King.json
├── McDonald's.json
├── KFC.json
├── Pizza Hut.json
├── Taco Bell.json
└── Wendy's.json
```

---

## 🧱 Modelagem OOP

| Classe | Descrição |
|--------|-----------|
| `Restaurante` | Gerencia nome, categoria, estado, cardápio e avaliações |
| `Avaliacao` | Armazena nota e cliente de cada avaliação |
| `ItemCardapio` | Classe base com nome e preço |
| `Prato` | Herda de `ItemCardapio`, adiciona descrição |
| `Bebida` | Herda de `ItemCardapio`, adiciona tamanho |

**Conceitos aplicados:** herança, encapsulamento, propriedades (`@property`), métodos de classe (`@classmethod`), `__str__`, leitura de JSON.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **JSON** — carregamento de dados externos
- **POO** — estrutura de classes com herança e encapsulamento
- **OS / CLI** — interface via terminal com limpeza de tela multiplataforma

---

## 🚀 Como Executar

### Pré-requisitos

```bash
python >= 3.9
```

### Instalação

```bash
# Clone o repositório
git clone https://github.com/ingridypinho/Restaurante.git

# Acesse a pasta
cd Restaurante

# Instale as dependências (opcional)
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

### Menu disponível

```
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
```

---

## 👩‍💻 Autora

**Ingridy Isabelli**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isapinho)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ingridypinho)
