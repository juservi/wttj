"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

def both_ends(s):
    if len(s)>1:
        result= ''.join([s[:2],s[-2:]])
    else:
        result = ''
    return result

#usando o while    

'''def both_ends(s):
    if len(s)>1:
        cont=0
        l=[]
        while cont<len(s):
            item = s[cont]
            l.append(item)
            cont+=1
        result = l[0]+l[1]+l[-2]+l[-1]

        #result=result_01[0]+result_01[1]+result_02[0]+result_02[1]
    else:
        result=''
    return result'''


print(both_ends('Spring'))
print(both_ends('Hello'))
print(both_ends('a'))
print(both_ends('xyz'))


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
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
