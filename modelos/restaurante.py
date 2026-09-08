from .avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        self._cardapio.append(item)

    def exibir_cardapio(self):
        if not self._cardapio:
            print(f"\n📋 Cardápio de {self._nome} está vazio!")
            return

        print(f"\n{'='*50}")
        print(f"📋 CARDÁPIO - {self._nome}")
        print(f"{'='*50}")
        for i, item in enumerate(self._cardapio, 1):
            if hasattr(item, 'descricao'):
                print(f"{i}. 🍽️  {item._nome} - R$ {item._preco:.2f}")
                print(f"   📝 {item.descricao}")
            elif hasattr(item, 'tamanho'):
                print(f"{i}. 🥤 {item._nome} - R$ {item._preco:.2f}")
                print(f"   📏 Tamanho: {item.tamanho}")
            else:
                print(f"{i}. 📦 {item._nome} - R$ {item._preco:.2f}")
        print(f"{'='*50}")
