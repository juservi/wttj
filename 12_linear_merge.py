"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def linear_merge(list1, list2):
    nova_fila=[]
    #-5,-4,-3,-2,-1
    fila_1 = list1
    fila_2 = list2

    inicio_1 = fila_1.pop(-1)
    inicio_2 = fila_2.pop(-1)

    if inicio_1 < inicio_2:
        nova_fila.append(inicio_1)
        nova_fila.append(inicio_2)

    while fila_1 and fila_2:
        elemento_final_fila_1 = fila_1.pop(-1)
        elemento_final_fila_2 = fila_2.pop(-1)

        if elemento_final_fila_1 < elemento_final_fila_2:

            nova_fila.insert(0,elemento_final_fila_1)
            nova_fila.insert(1,elemento_final_fila_1)
        elif elemento_final_fila_1 > elemento_final_fila_2:
            if elemento_final_fila_1 > nova_fila[-1] and elemento_final_fila_1 > nova_fila[-2]:


                nova_fila.insert(1,elemento_final_fila_1)
                nova_fila.insert(0,elemento_final_fila_1)
        else:
            nova_fila.insert(0,elemento_final_fila_1)
            nova_fila.insert(1,elemento_final_fila_1)

    if fila_1 and not fila_2:
        while True:
            if not fila_1:
                break
            elemento = fila_1.pop(-1)
            nova_fila.insert(0,elemento)
    
    if fila_2 and not fila_1:
        while True:
            if not fila_2:
                break
            elemento = fila_2.pop(-1)
            nova_fila.insert(0,elemento)

#['cc', zz']
#1+1 
#1

print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
