"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.

import sys

#a função open_file abre o arquivo txt e transforma suas linhas em uma lista de caracteres
def open_file(file):
    l=[]
    with open(file,'r') as fl:
        text = (fl.read().split())
        for letter in text:
            l.append(letter.lower())
    fl.close()
    return l 

#a função counter_words retorna uma collections que conta o número de ocorrências para cada
#caracter da lista retornada em def open_file
def counter_words(file):
    import collections
    from collections import Counter,OrderedDict
    letters = open_file(file)
    set_letters = set(letters)
    for i in set_letters:
        c = Counter(letters)
        return c

#a função print_words itera na collections de counter_words para retornar as ocorrências
#ordenadas pelas chaves.
def print_words(file):
    p_words = counter_words(file)
    for k,v in sorted(p_words.items()):
        print(k,v)


#a função print_top itera na collections de counter_words para retornar as ocorrências
# com a limitação de 20 
def print_top(file):
    common_words = counter_words(file)
    common = common_words.most_common(20)
    for k,v in common:
        print(k,v)

    
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
