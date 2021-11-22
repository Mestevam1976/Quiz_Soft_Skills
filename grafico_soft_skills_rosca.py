from typing import Any
import matplotlib.pyplot as plt

rotulos_Categorias = ['Importante', 'Urgente', 'Circunstancial']

list_data = [10, 60, 30]

grafico_rosca = plt.Circle((0,0), 0.7, color ='white')

fig = plt.figure('Quiz do Tempo')

plt.pie(list_data, labels = rotulos_Categorias, wedgeprops= {'linewidth': 7, 'edgecolor':'white'})

p= plt.gcf()

p.gca().add_artist(grafico_rosca)

plt.show()