# -*- coding: utf-8 -*-

# PUBLIC API:
#   count_prepositions
#   count_verbs
#   count_verbs_in_subjunctive_form
#   create_vocabulary_list
#   count_pretty_numbers

def count_prepositions(text):
    words = text.split(' ')
    counter = 0

    for word in words:
        if _is_preposition(word):
            counter += 1
    
    return counter


def count_verbs(text):
    words = text.split(' ')
    counter = 0

    for word in words:
        if _is_verb(word):
            counter += 1
    
    return counter


def count_verbs_in_subjunctive_form(text):
    words = text.split(' ')
    counter = 0

    for word in words:
        if _is_verb(word) and _is_verb_in_subjunctive_form(word):
            counter += 1
    
    return counter


def count_pretty_numbers(text):
    words = text.split(' ')
    unique_words = _remove_duplicate_items(words)
    numbers = _convert_to_decimal_numbers(unique_words)
    pretty_numbers = [n for n in numbers if n >= 422224 and n % 3 == 0]
    return len(pretty_numbers)


'''
    Cria a lista de vocabulário Booglan e a ordena em ordem lexicográfica.
'''
def create_vocabulary_list(str):
    words = str.split(' ')
    unique_words = _remove_duplicate_items(words)
    sorted_words = sorted(unique_words, cmp=_compare_booglan_alphabetical_order)
    sorted_str = ' '.join(sorted_words)
    return sorted_str


# HELPERS
ALPHABET_DICT = {
    't': 0, 'w': 1, 'h': 2,
    'z': 3, 'k': 4, 'd': 5,
    'f': 6, 'v': 7, 'c': 8,
    'j': 9, 'x': 10, 'l': 11,
    'r': 12, 'n': 13, 'q': 14,
    'm': 15, 'g': 16, 'p': 17,
    's': 18, 'b': 19
}

def _is_foo_letter(letter):
    return letter in 'rtcdb'


def _is_preposition(word):
    last_letter = word[-1]
    forbidden_letter = 'l'

    if len(word) != 5:
        return False
    
    if _is_foo_letter(last_letter):
        return False

    if forbidden_letter in word:
        return False

    return True


def _is_verb(word):
    last_letter = word[-1]

    # há um erro no enunciado. lá é dito que um verbo tem 7 letras ou mais.
    # se eu considerar isso há na verdade 144 verbos, não 71. 
    # se eu considerar que um verbo tem mais do que 7 letras ai sim é que existe 71 verbos.
    if len(word) <= 7:
        return False
    
    if _is_foo_letter(last_letter):
        return False

    return True


def _is_verb_in_subjunctive_form(verb):
    first_letter = verb[0]

    if _is_foo_letter(first_letter):
        return False
    
    return True


def _convert_to_decimal_numbers(numbers):
    decimal_numbers = []
    
    for number in numbers:
        digits = list(number)

        index = 0
        decimal_number = 0
        for digit in digits:
            value = ALPHABET_DICT[digit]
            multiplier_factor = 20 ** index
            partial = value * multiplier_factor
            decimal_number += partial
            index += 1

        decimal_numbers.append(decimal_number)
    
    return decimal_numbers


'''
    A função sorted([], cmp=function) da biblioteca padrão do Python ordena uma lista. Ela aceita
    como parâmetro uma função de comparação (cmp). Muitas linguagens possuem esse recurso e o Python é
    uma delas. A ideia dessa função de comparação é dizer para o sorted() COMO ele deve ordenar a lista.

    Funciona da seguinte forma:
        - Se a função de comparação retornar um número negativo quer dizer que "a" precede "b"
        - Se a função de comparação retornar um número positivo quer dizer que "b" precede "a"
        - Se a função de comparação retornar 0 quer dizer que ambos são iguais
    
    No caso aqui, a função de comparação é recursiva porque todas as letras da palavra me importa para 
    a ordenação, não só a primeira. Por isso, se encontro duas palavras que tem a primeira letra igual
    (abacaxi e abacate por exemplo) eu removo a primeira letra de ambas e prossigo para a próxima iteração
    até que encontre uma letra diferente ou até chegar o final da palavra.

    Mais detalhes na documentação:
    https://docs.python.org/2/howto/sorting.html#the-old-way-using-the-cmp-parameter
'''
def _compare_booglan_alphabetical_order(a, b):
    if a == '' and b == '':
        # "a" e "b" não trocam de lugar
        return 0
    elif a == '':
        # "a" vem primeiro que "b"
        return -1
    elif b == '':
        # "b" vem primeiro que "a"
        return 1

    diff = ALPHABET_DICT[a[0]] - ALPHABET_DICT[b[0]]

    if diff != 0:
        return diff
    else:
        return _compare_booglan_alphabetical_order(a[1:], b[1:])


'''
    Remove itens duplicados de uma lista
'''
def _remove_duplicate_items(lst): 
   return list(set(lst))
