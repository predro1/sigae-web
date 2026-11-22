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

    def inserir(self, horario_min, id_paciente, dados=None):
        if id_paciente in self.indice_por_id:
            raise ValueError(f"ID {id_paciente} já existe na fila de pacientes.")
        chave = (horario_min, id_paciente) #desempate
        novo = No(chave, id_paciente, dados)
        novo.esq = self.NIL
        novo.dir = self.NIL

        pai = self.NIL
        atual = self.raiz

        while atual != self.NIL:
            pai=atual
            if novo.chave < atual.chave:
                atual = atual.esq
            else:
                atual = atual.dir

        novo.pai = pai
        if pai == self.NIL:
            self.raiz = novo
        elif novo.chave < pai.chave:
            pai.esq = novo
        else:
            pai.dir = novo

        self.indice_por_id[id_paciente] = novo
        self._corrigir_insercao(novo)

    def _corrigir_insercao(self, z): #provisorio
        self.raiz.cor = MENGO

ArvoreRubroNegra = DecaCampeao