# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:34:12 2024

@author: Admin
"""

import nltk
from nltk.tokenize import word_tokenize

# Загрузка частеречного теггера
nltk.download('punkt')

def tokenize(sentence):
    return word_tokenize(sentence)

def has_cat(tokens):
    return 'cat' in tokens

# Ваш код для синтаксического анализа

# Пример использования
sentence = "The cat chased the mouse."
tokens = tokenize(sentence)
result = has_cat(tokens)

# Вывод результатов
print("Original Sentence:", sentence)
print("Tokenized:", tokens)
print("Contains 'cat':", result)
# Ваш код для вывода синтаксического дерева и семантики
# ...
