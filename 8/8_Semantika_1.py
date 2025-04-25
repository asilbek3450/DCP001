# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:30:44 2024

@author: Admin
"""

import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Загрузка частеречного теггера
nltk.download('averaged_perceptron_tagger')

# Функция для токенизации предложения
def tokenize(sentence):
    return word_tokenize(sentence)

# Функция для определения частей речи
def pos_tagging(tokens):
    return pos_tag(tokens)

# Пример грамматики для синтаксического анализа
grammar = r"""
    NP: {<DT>?<JJ>*<NN>}  # Существительная группа
    VP: {<VB.*><NP>}  # Глагольная группа
    S: {<NP><VP>}  # Полное предложение
"""

# Функция для синтаксического анализа
def parse_syntax(tokens):
    cp = nltk.RegexpParser(grammar)
    return cp.parse(tokens)

# Функция для извлечения семантики из синтаксического дерева
def extract_semantics(tree):
    meaning = {}
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            # Извлечение семантики существительной группы
            meaning['NP'] = extract_noun_phrase(subtree)
        elif subtree.label() == 'VP':
            # Извлечение семантики глагольной группы
            meaning['VP'] = extract_verb_phrase(subtree)
    return meaning

# Пример функции для извлечения семантики существительной группы
def extract_noun_phrase(subtree):
    # Ваш код для извлечения семантики существительной группы
    return {'NounPhrase': 'NounPhraseMeaning'}

# Пример функции для извлечения семантики глагольной группы
def extract_verb_phrase(subtree):
    # Ваш код для извлечения семантики глагольной группы
    return {'VerbPhrase': 'VerbPhraseMeaning'}

# Пример использования
sentence = "The cat chased the mouse."
tokens = tokenize(sentence)
tags = pos_tagging(tokens)
syntax_tree = parse_syntax(tags)
semantics = extract_semantics(syntax_tree)

print("Original Sentence:", sentence)
print("Tokenized:", tokens)
print("POS Tags:", tags)
print("Syntax Tree:", syntax_tree)
print("Semantics:", semantics)
