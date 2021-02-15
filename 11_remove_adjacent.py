"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    result = []
    from itertools import zip_longest, islice
    '''criou duas variáveis f first s second
    o zip se baseia na lista menor. O zip_longest se baseia na maior.
    No caso da lista [1,2,2,3]:
    Na primeira rodada do laço for, nos parâmetros de zip_longest, em nums ele pega o 
    número 1 e o slice pega o 2 (o número 1 indica para pegar no índice 1) e o None é
    para o caso do número de elementos entre as listas serem diferentes.
    Então nas rodadas do for ele monta as tuplas (1,2),(2,2),(2,3).
    Se dentro das tuplas os elementos forem diferentes, vão para a nova lista. 
    Senão não entra'''  
    for f, s in zip_longest(nums, islice(nums, 1, None)):
        if f != s:
            result.append(f)
    return result
    
print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([]))
print(remove_adjacent([2, 2, 3, 3, 3, 2, 2]))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
