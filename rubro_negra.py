FLA, MENGO = 0, 1
#RUBRO = FLA. NEGRO = MENGO
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

    def _corrigir_insercao(self, z):
        while z.pai != self.NIL and z.pai.cor == FLA: #quando tiver dois rubros seguidos
            avo = z.pai.pai

            if z.pai == avo.esq:
                tio = avo.dir
                if tio.cor == FLA:     #caso 1: pai e tio rubro. recolore
                    z.pai.cor = MENGO
                    tio.cor = MENGO
                    avo.cor = FLA
                    z = avo
                else:                  #caso 2 tio negro e nó em zig zag. rotaciona
                    if z == z.pai.dir:
                        z = z.pai
                        self._rot_esq(z)

                    z.pai.cor = MENGO  #caso 3: tio negro e nós em linha reta. recolore e rotaciona
                    avo.cor = FLA
                    self._rot_dir(avo)
            else:
                tio = avo.esq      #quando tiver espelhado
                if tio.cor == FLA:     # caso 1
                    z.pai.cor = MENGO
                    tio.cor = MENGO
                    avo.cor = FLA
                    z = avo
                else:                  # caso 2
                    if z == z.pai.esq:
                        z = z.pai
                        self._rot_dir(z)

                    z.pai.cor = MENGO  #caso 3
                    avo.cor = FLA
                    self._rot_esq(avo)

        self.raiz.cor = MENGO #regra 2: raiz sempre negra

    def ordem(self):
        resultado = []

        def _percorre(no):
            if no == self.NIL:
                return
            _percorre(no.esq)
            resultado.append({
                "id": no.id,
                "chave": no.chave,
                "cor": "FLA" if no.cor == FLA else "MENGO",
                "dados": no.dados
            })
            _percorre(no.dir)

        _percorre(self.raiz)
        return resultado

    def buscar_id(self, id_paciente):

        no = self.indice_por_id.get(id_paciente)
        if not no or no == self.NIL:
            return None
        return {
            "id": no.id,
            "chave": no.chave,
            "cor": "FLA" if no.cor == FLA else "MENGO",
            "dados": no.dados
        }

    def buscar_horario(self, horario_min):
        encontrados = []
        def _buscar(no):
            if no == self.NIL:
                return
            hora_no = no.chave[0]
            if horario_min < hora_no:
                _buscar(no.esq)
            elif horario_min > hora_no:
                _buscar(no.dir)
            else:
                _buscar(no.esq)
                encontrados.append({
                    "id": no.id,
                    "chave": no.chave,
                    "cor": "FLA" if no.cor == FLA else "MENGO",
                    "dados": no.dados
                })
                _buscar(no.dir)

        _buscar(self.raiz)
        return encontrados


    def _transplantar(self, u, v):  #Substitui a subárvore enraizada em u pela subárvore enraizada em v.
        if u.pai == self.NIL:
            self.raiz = v
        elif u == u.pai.esq:
            u.pai.esq = v
        else:
            u.pai.dir = v
        v.pai = u.pai

    def _minimo(self, no):          #Retorna o nó com a menor chave (mais à esquerda) a partir de um nó.
        while no.esq != self.NIL:
            no = no.esq
        return no

    def remover(self, id_paciente): #Remove um paciente da fila pelo ID em O(log n) e rebalanceia a árvore.
        z = self.indice_por_id.get(id_paciente)
        if not z or z == self.NIL:
            raise ValueError(f"ID {id_paciente} não encontrado na fila de pacientes.")

        del self.indice_por_id[id_paciente]

        y = z
        cor_original_y = y.cor

        if z.esq == self.NIL:
            x = z.dir
            self._transplantar(z, z.dir)
        elif z.dir == self.NIL:
            x = z.esq
            self._transplantar(z, z.esq)
        else:
            y = self._minimo(z.dir)
            cor_original_y = y.cor
            x = y.dir
            if y.pai == z:
                x.pai = y
            else:
                self._transplantar(y, y.dir)
                y.dir = z.dir
                y.dir.pai = y

            self._transplantar(z, y)
            y.esq = z.esq
            y.esq.pai = y
            y.cor = z.cor

        if cor_original_y == MENGO:
            self._corrigir_remocao(x)

    def _corrigir_remocao(self, x):
        while x != self.raiz and x.cor == MENGO:
            if x == x.pai.esq:
                irmao = x.pai.dir
                if irmao.cor == FLA:   # Caso 1: irmão rubro -> rotaciona e vira Caso 2, 3 ou 4
                    irmao.cor = MENGO
                    x.pai.cor = FLA
                    self._rot_esq(x.pai)
                    irmao = x.pai.dir

                if irmao.esq.cor == MENGO and irmao.dir.cor == MENGO: # Caso 2: irmão e sobrinhos negros
                    irmao.cor = FLA
                    x = x.pai
                else:
                    if irmao.dir.cor == MENGO: # Caso 3: irmão negro, sobrinho esquerdo rubro
                      irmao.esq.cor = MENGO
                      irmao.cor = FLA
                      self._rot_dir(irmao)
                      irmao = x.pai.dir

                    irmao.cor = x.pai.cor      # Caso 4: irmão negro, sobrinho direito rubro
                    x.pai.cor = MENGO
                    irmao.dir.cor = MENGO
                    self._rot_esq(x.pai)
                    x = self.raiz
            else:
                irmao = x.pai.esq   #espelhado
                if irmao.cor == FLA: # Caso 1
                    irmao.cor = MENGO
                    x.pai.cor = FLA
                    self._rot_dir(x.pai)
                    irmao = x.pai.esq

                if irmao.dir.cor == MENGO and irmao.esq.cor == MENGO:  # Caso 2
                    irmao.cor = FLA
                    x = x.pai
                else:
                    if irmao.esq.cor == MENGO:  # Caso 3
                        irmao.dir.cor = MENGO
                        irmao.cor = FLA
                        self._rot_esq(irmao)
                        irmao = x.pai.esq

                    # Caso 4
                    irmao.cor = x.pai.cor
                    x.pai.cor = MENGO
                    irmao.esq.cor = MENGO
                    self._rot_dir(x.pai)
                    x = self.raiz

        x.cor = MENGO

ArvoreRubroNegra = DecaCampeao