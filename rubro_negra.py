FLA, MENGO = 0, 1

class No:
    def __init__(self, chave, id_paciente=None, dados=None):
        self.chave = chave
        self.id = id_paciente
        self.dados = dados
        self.cor = FLA
        self.esq = None
        self.dir = None
        self.pai = None

class DecaCampeao: #Arvore Rubro Negra
    def __init__(self):
        self.NIL = No(chave=None)
        self.NIL.cor = MENGO
        self.NIL.esq = self.NIL
        self.NIL.dir = self.NIL
        self.NIL.pai = self.NIL
        self.raiz = self.NIL
        self.indice_por_id = {}
        self.rotacoes = 0

ArvoreRubroNegra = DecaCampeao