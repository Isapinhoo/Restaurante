# Sabores Express — gestão de restaurantes em Python

Aplicação de linha de comando para cadastrar restaurantes, montar cardápio e registrar avaliações. Exercício de programação orientada a objetos: herança, properties e encapsulamento.

O projeto tem como base o curso de POO com Python da Alura. Sobre a estrutura do curso, acrescentei a carga dos cardápios a partir de arquivos JSON, a classificação automática de bebida ou prato por palavra-chave no nome do item, e a inferência de tamanho da bebida.

Sobre os dados: os seis arquivos JSON trazem nomes de itens de cardápios reais, mas os preços e as descrições são gerados — os preços caem todos entre R$ 30 e R$ 60, independente do item, e as descrições se repetem em ciclo. Servem para exercitar o código, não para análise.

## Modelagem

```
ItemCardapio (classe base)
    Prato    -> acrescenta descricao
    Bebida   -> acrescenta tamanho

Restaurante -> tem N itens de cardápio e N avaliacoes
Avaliacao   -> cliente e nota
```

`Prato` e `Bebida` herdam de `ItemCardapio` e chamam `super().__init__()` para nome e preço, acrescentando só o que é próprio de cada um. É por isso que `exibir_cardapio` consegue tratar os dois na mesma lista.

Os atributos de `Restaurante` são privados por convenção e o acesso de fora passa por property: `nome`, `categoria`, `esta_ativo` e `media_avaliacoes` são somente leitura, e mudar o estado exige chamar `alternar_estado()`. Isso evita que quem usa a classe ligue um restaurante escrevendo direto no atributo e passe por cima de qualquer regra futura.

`media_avaliacoes` é property e não atributo porque a média é derivada: recalcula a cada leitura em vez de guardar um valor que ficaria desatualizado a cada nova avaliação. Com a lista vazia devolve `'-'`, para a tabela não quebrar em restaurante sem nota.

`receber_avaliacao` valida a nota entre 1 e 5 antes de criar a `Avaliacao`. A validação fica na classe, não na interface, então vale para qualquer chamada.

## Estrutura

```
Restaurante/
├── main.py                        interface de terminal e carga dos JSONs
├── modelos/
│   ├── restaurante.py             classe Restaurante
│   ├── avaliacao.py               classe Avaliacao
│   └── cardapio/
│       ├── item_cardapio.py       classe base
│       ├── prato.py               herda de ItemCardapio
│       └── bebida.py              herda de ItemCardapio
├── Burger King.json               cardápios usados na carga inicial
├── KFC.json
├── McDonald's.json
├── Pizza Hut.json
├── Taco Bell.json
├── Wendy's.json
└── requirements.txt
```

## Como rodar

Requisitos: Python 3.10 ou superior.

```bash
git clone https://github.com/Isapinhoo/Restaurante.git
cd Restaurante
python main.py
```

Não precisa instalar nada: o projeto usa só a biblioteca padrão. O `requirements.txt` está no repositório por conta do ambiente original.

Ao abrir, os seis cardápios são carregados e cada restaurante entra com cinco itens. O menu tem sete opções: listar, cadastrar, ativar ou desativar, avaliar, ver cardápio, adicionar item e sair.

## Próximos passos

- [ ] Persistir os restaurantes cadastrados, hoje tudo se perde ao fechar
- [ ] Testes com pytest para as regras de nota e média
- [ ] Deixar a quantidade de itens carregados configurável, em vez de fixa em cinco
- [ ] Tratar erro de carga por arquivo, em vez de um `except Exception` genérico

## Autora

Ingridy Isabelli Sant'Ana de Pinho — Sistemas de Informação, Universidade Anhembi Morumbi.

[LinkedIn](https://www.linkedin.com/in/isapinho) · [GitHub](https://github.com/Isapinhoo)
