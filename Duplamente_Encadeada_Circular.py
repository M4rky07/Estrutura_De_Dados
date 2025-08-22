class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.primeiro = None

    def criarNovoElemento(self, valor):
        return Elemento(valor)

    def imprimeLista(self):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        atual = self.primeiro
        while True:
            print(atual.valor)
            atual = atual.proximo
            if atual == self.primeiro:
                break

    def addElementoNoFinal(self, valor):
        novo = self.criarNovoElemento(valor)
        if self.primeiro is None:
            self.primeiro = novo
            novo.proximo = novo
            novo.anterior = novo
        else:
            ultimo = self.primeiro.anterior
            ultimo.proximo = novo
            novo.anterior = ultimo
            novo.proximo = self.primeiro
            self.primeiro.anterior = novo

    def addElementoNoInicio(self, valor):
        novo = self.criarNovoElemento(valor)
        if self.primeiro is None:
            self.primeiro = novo
            novo.proximo = novo
            novo.anterior = novo
        else:
            ultimo = self.primeiro.anterior
            novo.proximo = self.primeiro
            novo.anterior = ultimo
            ultimo.proximo = novo
            self.primeiro.anterior = novo
            self.primeiro = novo

    def removeElementoNoFinal(self):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        if self.primeiro.proximo == self.primeiro:
            # Só existe um elemento na lista
            self.primeiro = None
            print("--- Lista Vazia novamente ---")
        else:
            ultimo = self.primeiro.anterior
            penultimo = ultimo.anterior
            penultimo.proximo = self.primeiro
            self.primeiro.anterior = penultimo
            del ultimo
