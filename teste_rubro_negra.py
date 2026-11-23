from rubro_negra import DecaCampeao


def rodar_testes():
    fila = DecaCampeao()

    # 1. Inserção de pacientes (incluindo empate de horário às 08:30 -> 510 min)
    pacientes = [
        (540, 101, {"nome": "Carlos Silva", "prioridade": "Normal"}),      # 09:00
        (480, 102, {"nome": "Ana Souza", "prioridade": "Urgente"}),        # 08:00
        (510, 105, {"nome": "Bruno Lima", "prioridade": "Normal"}),        # 08:30 (ID maior)
        (510, 103, {"nome": "Mariana Costa", "prioridade": "Normal"}),     # 08:30 (ID menor)
        (600, 104, {"nome": "Pedro Santos", "prioridade": "Retorno"}),     # 10:00
        (450, 106, {"nome": "Lucia Alves", "prioridade": "Emergencia"}),   # 07:30
    ]

    for horario, id_pac, dados in pacientes:
        fila.inserir(horario, id_pac, dados)

    status = fila.validar()
    assert status["valida"] is True
    assert status["total_pacientes"] == 6
    print("1. Inserção e validação inicial OK:", status)

    # 2. Teste de bloqueio de ID duplicado
    try:
        fila.inserir(520, 101, {"nome": "Duplicado"})
        assert False, "Deveria ter bloqueado ID duplicado!"
    except ValueError as erro:
        print("2. Bloqueio de ID duplicado OK:", erro)

    # 3. Percurso em ordem cronológica (com desempate por ID)
    ordenados = fila.ordem()
    chaves = [p["chave"] for p in ordenados]
    assert chaves == [
        (450, 106),
        (480, 102),
        (510, 103),
        (510, 105),
        (540, 101),
        (600, 104),
    ]
    print("3. Ordenação cronológica e desempate OK:", chaves)

    # 4. Busca O(1) por ID e O(log n) por horário
    pac_103 = fila.buscar_id(103)
    assert pac_103 is not None and pac_103["dados"]["nome"] == "Mariana Costa"

    pac_0830 = fila.buscar_horario(510)
    assert len(pac_0830) == 2
    print("4. Buscas por ID e horário OK.")

    # 5. Remoções (folha, nó com 1 filho e nó com 2 filhos/raiz) + revalidação
    for id_remover in [106, 102, 101, 103]:
        fila.remover(id_remover)
        status = fila.validar()
        assert status["valida"] is True

    assert fila.buscar_id(101) is None
    assert len(fila.ordem()) == 2
    print("5. Remoções e rebalanceamento OK:", fila.validar())


if __name__ == "__main__":
    rodar_testes()