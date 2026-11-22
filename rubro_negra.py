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

    def _rot_esq(self, x):
        y = x.dir
        x.dir = y.esq
        if y.esq != self.NIL:
            y.esq.pai = x

        y.pai = x.pai
        if x.pai == self.NIL:
            self.raiz = y
        elif x == x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y

        y.esq = x
        x.pai = y
        self.rotacoes +=1

    def _rot_dir(self, y):
        x = y.esq
        y.esq = x.dir
        if x.dir != self.NIL:
            x.dir.pai = y

        x.pai = y.pai
        if y.pai == self.NIL:
            self.raiz = x
        elif y == y.pai.dir:
            y.pai.dir = x
        else:
            y.pai.esq = x

        x.dir = y
        y.pai = x
        self.rotacoes +=1



ArvoreRubroNegra = DecaCampeao