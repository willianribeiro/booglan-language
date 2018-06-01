# -*- coding: utf-8 -*-
# This module is a service to deal with Booglan texts.
#
# Public API:
#   count_prepositions(text)
#   count_verbs(text)
#   count_verbs_in_subjunctive_form(text)
#   count_pretty_numbers(text)
#   create_vocabulary_list(text)

def count_prepositions(text):
    '''
        Counts the number of prepositions in a string.
        Args:
            text: the string to be counted.
        Returns:
            Integer: total of prepositions.
    '''
    words = text.split(' ')
    counter = 0

    for word in words:
        if _is_preposition(word):
            counter += 1
    
    return counter

def count_verbs(text):
    '''
        Counts the number of verbs in a string.
        Args:
            text: the string to be counted.
        Returns:
            Integer: total of verbs.
    '''
    words = text.split(' ')
    counter = 0

    for word in words:
        if _is_verb(word):
            counter += 1
    
    return counter

def count_verbs_in_subjunctive_form(text):
    '''
        Counts the number of verbs in subjunctive form in a string.
        Args:
            text: the string to be counted.
        Returns:
            Integer: total of verbs in subjunctive form.
    '''
    words = text.split(' ')
    counter = 0

    for word in words:
        if _is_verb(word) and _is_verb_in_subjunctive_form(word):
            counter += 1
    
    return counter


def count_pretty_numbers(text):
    '''
        Counts the number of pretty numbers in a string.
        Args:
            text: the string to be counted.
        Returns:
            Integer: total of pretty numbers.
    '''
    words = text.split(' ')
    unique_words = _remove_duplicated_items(words)
    numbers = _convert_to_decimal_numbers(unique_words)
    pretty_numbers = [n for n in numbers if _is_pretty_number(n)]
    return len(pretty_numbers)


def create_vocabulary_list(text):
    '''
        Create a vocabulary list (without duplicate words) and sort in a 
        lexicographic order.
        Args:
            text: the string from which the list will be created.
        Returns:
            string: a string with unique words ordered lexicographically
    '''
    words = text.split(' ')
    unique_words = _remove_duplicated_items(words)
    sorted_words = sorted(unique_words, cmp=_compare_booglan_alphabetical_order)
    sorted_text = ' '.join(sorted_words)
    return sorted_text


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
    if not word:
        return False

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
    if not word:
        return False

    last_letter = word[-1]

    if len(word) < 8:
        return False
    
    if _is_foo_letter(last_letter):
        return False

    return True


def _is_verb_in_subjunctive_form(verb):
    if not verb:
        return False

    first_letter = verb[0]

    if _is_foo_letter(first_letter):
        return False
    
    return True

def _is_pretty_number(number):
    return number >= 422224 and number % 3 == 0

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

def _compare_booglan_alphabetical_order(a, b):
    '''
        Then function sorted([], cmp=function) from the Python Standard Library
        sorts a list. It receives a comparation function (cmp). A lot of 
        programming languages has this feature and Python is one of them. The
        idea of this comparation function is say to sorted() HOW it should sort
        the list.

        It works as follow:
            - If the comparation function returns a negative number it means
            that "a" precedes "b".
            - If the comparation function returns a positive number it means
            that "b" precedes "a".
            - If the comparation function returns 0 it means both are equals.

        In this case, the comparation function is recursive because all the 
        letter of the word must be considered, not only the first one.

        More details on docs:
        https://docs.python.org/2/howto/sorting.html#the-old-way-using-the-cmp-parameter
    '''
    if a == '' and b == '':
        # "a" and "b" must be equals
        return 0
    elif a == '':
        # "a" comes first then "b"
        return -1
    elif b == '':
        # "b" comes first than "a"
        return 1

    diff = ALPHABET_DICT[a[0]] - ALPHABET_DICT[b[0]]

    if diff != 0:
        return diff
    else:
        return _compare_booglan_alphabetical_order(a[1:], b[1:])

def _remove_duplicated_items(lst):
   return list(set(lst))
