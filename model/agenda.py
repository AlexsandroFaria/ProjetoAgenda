class Agenda:
    def __init__(self, id_agenda=None, nome=None, sobrenome=None, endereco=None, numero=None, complemento=None, bairro=None,
                 uf=None, data=None):
        self._id_agenda = id_agenda
        self._nome = nome
        self._sobrenome = sobrenome
        self._endereco = endereco
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._uf = uf
        self._data = data

    @property
    def id_agenda(self):
        return self._id_agenda

    @id_agenda.setter
    def id_agenda(self, valor):
        self._id_agenda = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, valor):
        self._complemento = valor

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, valor):
        self._bairro = valor

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, valor):
        self._uf = valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor):
        self._data = valor
