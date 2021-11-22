from typing import Any
import matplotlib.pyplot as plt
from os import system, name # importa informações sobre o sistema operacional em uso
import formatacao, mensagens, funcoes

def clear(): # limpa a tela removendo do prompt as informações anteriores ao código

  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def grafico():
  rotulos_Categorias = [['Importante {:.1%}'.format(importante/total)], ['Urgente {:.1%}'.format(urgente/total)], ['Circunstancial {:.1%}'.format(circunstancial/total)]]

  list_data = [importante, urgente, circunstancial]

  grafico_rosca = plt.Circle((0,0), 0.7, color ='white')

  fig = plt.figure('Quiz do Tempo')

  plt.pie(list_data, labels = rotulos_Categorias, wedgeprops= {'linewidth': 8, 'edgecolor':'white'})

  p= plt.gcf()

  p.gca().add_artist(grafico_rosca)

  plt.show()

clear()
print('=' * 75)
print(mensagens.frase_01.center(75))
formatacao.forma_linha()
print('Responda as 15 perguntas à seguir: ')
print('=' * 75)

funcoes.questao_01()
total = (sum((funcoes.a) + (funcoes.b) + (funcoes.c)))
importante = sum(funcoes.a)
urgente = sum(funcoes.b)
circunstancial = sum(funcoes.c)

formatacao.forma_linha()
print(' O PERCENTUAL DE PONTOS COMO IMPORTANTE É DE: {:.1%}'.format(importante/total))
print('\n')
print(' O PERCENTUAL DE PONTOS COMO URGENTE É DE: {:.1%}'.format(urgente/total))
print('\n')
print(' O PERCENTUAL DE PONTOS COMO CIRCUNSTANCIAL É DE: {:.1%}'.format(circunstancial/total))
formatacao.forma_linha()
grafico()



