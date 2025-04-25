# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:18:43 2024

@author: Admin
"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Загрузим датасет Iris
iris = load_iris()
X = iris.data
y = iris.target

# Стандартизируем данные
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Разделим данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Преобразуем данные в тензоры PyTorch
X_train_tensor = torch.FloatTensor(X_train)
X_test_tensor = torch.FloatTensor(X_test)
y_train_tensor = torch.LongTensor(y_train)
y_test_tensor = torch.LongTensor(y_test)

# Определение нейронной сети
class IrisClassifier(nn.Module):
    def __init__(self):
        super(IrisClassifier, self).__init__()
        self.fc1 = nn.Linear(4, 8)  # Входной слой: 4 признака, 8 нейронов
        self.relu = nn.ReLU()      # Функция активации ReLU
        self.fc2 = nn.Linear(8, 3)  # Выходной слой: 3 класса (Iris setosa, versicolor, virginica)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Инициализация модели, функции потерь и оптимизатора
model = IrisClassifier()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Обучение модели
epochs = 100
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}')

# Оценка модели на тестовом наборе
with torch.no_grad():
    outputs = model(X_test_tensor)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y_test_tensor).sum().item() / len(y_test_tensor)
    print(f'Test Accuracy: {accuracy * 100:.2f}%')


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
