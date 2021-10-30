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

import sys


def open_file(filename):
    with open(filename, mode='r') as file:
        raw_list = file.readlines()

    elements = []
    for line in raw_list:
        temp_list = line.split()
        for letter in temp_list:
            elements.append(letter.lower())

    return elements


def words_dict(letter_list):
    sort_list = sorted(letter_list)
    word_dict = dict.fromkeys(sorted(set(letter_list)), 0)

    for vowel in set(letter_list):
        word_dict[vowel] = sort_list.count(vowel)

    return word_dict


def print_words(filename):
    letter_list = open_file(filename)
    letter_dict = words_dict(letter_list)

    for letter, occur in letter_dict.items():
        print(letter, occur)


def print_top(filename):
    letter_list = open_file(filename)
    letter_dict = words_dict(letter_list)

    inverse_dict = dict(sorted(letter_dict.items(), reverse=True, key=lambda x: x[1]))

    count = 1
    for letter, occur in inverse_dict.items():
        if count == 21:
            break
        print(f"Line {count}: {letter} {occur}")
        count += 1
# A função abaixo chama print_words() ou print_top() de acordo com os
# parâmetros do programa.


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
