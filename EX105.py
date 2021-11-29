def notas(*nota, sit=False):
    """
    Notas é uma função para escrever o desempenho do aluno.
    :param nota: Todas as notas.
    :param sit: Se deseja obter a situação do aluno.
    :return: Quantas notas, maior nota, menor nota, média, situação (OPCIONAL)
    """
    biblioteca = {}
    s = 0
    for c in nota:
        s += c
    biblioteca['Quantidade de notas'] = len(nota)
    biblioteca['Nota Máxima'] = max(nota)
    biblioteca['Nota Mínima'] = min(nota)
    media = s / len(nota)
    biblioteca['Média'] = media
    if sit:
        if media > 7:
            biblioteca['Situação'] = 'Aprovado!'
        elif 5 < media < 7:
            biblioteca['Situação'] = 'Recuperação!'
        elif media < 5:
            biblioteca['Situação'] = 'Reprovado!'
    for k, v in biblioteca.items():
        print(f'{k}: {v}')


notas(9, 10, 9, 4, sit=True)
