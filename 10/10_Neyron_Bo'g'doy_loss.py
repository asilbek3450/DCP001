# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:32:10 2024

@author: Admin
"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Загрузим датасет с семенами пшеницы
seeds = fetch_openml(name='seeds')
X = seeds.data
y = seeds.target.astype(int)

# Стандартизируем данные
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Разделим данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Преобразуем данные в тензоры PyTorch
X_train_tensor = torch.FloatTensor(X_train)
X_test_tensor = torch.FloatTensor(X_test)

# Преобразуем метки классов в тензоры PyTorch
label_encoder = LabelEncoder()
y_train_tensor = torch.LongTensor(label_encoder.fit_transform(y_train))
y_test_tensor = torch.LongTensor(label_encoder.transform(y_test))

# Определение нейронной сети
class SeedClassifier(nn.Module):
    def __init__(self):
        super(SeedClassifier, self).__init__()
        self.fc1 = nn.Linear(7, 8)  # Входной слой: 7 признаков, 8 нейронов
        self.relu = nn.ReLU()      # Функция активации ReLU
        self.fc2 = nn.Linear(8, 3)  # Выходной слой: 3 класса (сорта семян)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Инициализация модели, функции потерь и оптимизатора
model = SeedClassifier()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Обучение модели
epochs = 100
losses = []  # Добавляем список для сохранения значений функции потерь

for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}')
    
    losses.append(loss.item())  # Сохраняем значение функции потерь

# Визуализация графика функции потерь
plt.plot(losses)
plt.title('Training Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

# Оценка модели на тестовом наборе
with torch.no_grad():
    outputs = model(X_test_tensor)
    _, predicted = torch.max(outputs, 1)
    accuracy = accuracy_score(y_test_tensor, predicted)
    precision = precision_score(y_test_tensor, predicted, average='weighted')
    recall = recall_score(y_test_tensor, predicted, average='weighted')
    f1 = f1_score(y_test_tensor, predicted, average='weighted')

    print(f'Test Accuracy: {accuracy * 100:.2f}%')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1 Score: {f1:.2f}')

    # Confusion Matrix
    cm = confusion_matrix(y_test_tensor, predicted)
    print('Confusion Matrix:')
    print(cm)
# ... (остальной код для оценки модели и построения матрицы путаницы)
