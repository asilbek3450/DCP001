# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:50:50 2024

@author: Admin
"""

from textblob import TextBlob

text = "Компьютерная лингвистика очень увлекательная тема!"

blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print("Положительная тональность")
elif sentiment < 0:
    print("Отрицательная тональность")
else:
    print("Нейтральная тональность")
