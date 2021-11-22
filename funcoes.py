from os import system, name # importa informações sobre o sistema operacional em uso
import formatacao, mensagens

a = []
b = []
c = []

def clear(): # limpa a tela removendo do prompt as informações anteriores ao código
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def questao_01():
  proxima_pergunta = False
  while proxima_pergunta == False:
    print(mensagens.perguntas[0].upper())
    mensagens.opcoes()
    escolha_Q1 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q1 == 1 or escolha_Q1 == 2 or escolha_Q1 == 3 or escolha_Q1 == 4 or escolha_Q1 == 5:
      clear()
      proxima_pergunta = True
      b.append(escolha_Q1)
      questao_02()
      return escolha_Q1

    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))

      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5 or continua == ' ':
        proxima_pergunta = False
        clear()
  
def questao_02():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[1].upper())
    mensagens.opcoes()
    escolha_Q2 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q2 == 1 or escolha_Q2 == 2 or escolha_Q2 == 3 or escolha_Q2 == 4 or escolha_Q2 == 5:
      clear()
      proxima_pergunta = True
      b.append(escolha_Q2)
      questao_03()
      return escolha_Q2
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()
      
def questao_03():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[2].upper())
    mensagens.opcoes()
    escolha_Q3 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q3 == 1 or escolha_Q3 == 2 or escolha_Q3 == 3 or escolha_Q3 == 4 or escolha_Q3 == 5:
      clear()
      proxima_pergunta = True
      a.append(escolha_Q3)
      questao_04()
      return escolha_Q3
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_04():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[3].upper())
    mensagens.opcoes()
    escolha_Q4 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q4 == 1 or escolha_Q4 == 2 or escolha_Q4 == 3 or escolha_Q4 == 4 or escolha_Q4 == 5:
      clear()
      proxima_pergunta = True
      a.append(escolha_Q4)
      questao_05()
      return escolha_Q4
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_05():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[4].upper())
    mensagens.opcoes()
    escolha_Q5 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q5 == 1 or escolha_Q5 == 2 or escolha_Q5 == 3 or escolha_Q5 == 4 or escolha_Q5 == 5:
      clear()
      proxima_pergunta = True
      c.append(escolha_Q5)
      questao_06()
      return escolha_Q5
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_06():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[5].upper())
    mensagens.opcoes()
    escolha_Q06 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q06 == 1 or escolha_Q06 == 2 or escolha_Q06 == 3 or escolha_Q06 == 4 or escolha_Q06 == 5:
      clear()
      proxima_pergunta = True
      b.append(escolha_Q06)
      questao_07()
      return escolha_Q06
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_07():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[6].upper())
    mensagens.opcoes()
    escolha_Q7 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q7 == 1 or escolha_Q7 == 2 or escolha_Q7 == 3 or escolha_Q7 == 4 or escolha_Q7 == 5:
      clear()
      proxima_pergunta = True
      b.append(escolha_Q7)
      questao_08()
      return escolha_Q7
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_08():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[7].upper())
    mensagens.opcoes()
    escolha_Q8 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q8 == 1 or escolha_Q8 == 2 or escolha_Q8 == 3 or escolha_Q8 == 4 or escolha_Q8 == 5:
      clear()
      proxima_pergunta = True
      c.append(escolha_Q8)
      questao_09()
      return escolha_Q8
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_09():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[8].upper())
    mensagens.opcoes()
    escolha_Q9 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q9 == 1 or escolha_Q9 == 2 or escolha_Q9 == 3 or escolha_Q9 == 4 or escolha_Q9 == 5:
      clear()
      proxima_pergunta = True
      a.append(escolha_Q9)
      questao_10()
      return escolha_Q9
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_10():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[9].upper())
    mensagens.opcoes()
    escolha_Q10 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q10 == 1 or escolha_Q10 == 2 or escolha_Q10 == 3 or escolha_Q10 == 4 or escolha_Q10 == 5:
      clear()
      proxima_pergunta = True
      a.append(escolha_Q10)
      questao_11()
      return escolha_Q10
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_11():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[10].upper())
    mensagens.opcoes()
    escolha_Q11 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q11 == 1 or escolha_Q11 == 2 or escolha_Q11 == 3 or escolha_Q11 == 4 or escolha_Q11 == 5:
      clear()
      proxima_pergunta = True
      c.append(escolha_Q11)
      questao_12()
      return escolha_Q11
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_12():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[11].upper())
    mensagens.opcoes()
    escolha_Q12 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q12 == 1 or escolha_Q12 == 2 or escolha_Q12 == 3 or escolha_Q12 == 4 or escolha_Q12 == 5:
      clear()
      proxima_pergunta = True
      a.append(escolha_Q12)
      questao_13()
      return escolha_Q12
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_13():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[12].upper())
    mensagens.opcoes()
    escolha_Q13 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q13 == 1 or escolha_Q13 == 2 or escolha_Q13 == 3 or escolha_Q13 == 4 or escolha_Q13 == 5:
      clear()
      proxima_pergunta = True
      b.append(escolha_Q13)
      questao_14()
      return escolha_Q13
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_14():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[13].upper())
    mensagens.opcoes()
    escolha_Q14 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q14 == 1 or escolha_Q14 == 2 or escolha_Q14 == 3 or escolha_Q14 == 4 or escolha_Q14 == 5:
      clear()
      proxima_pergunta = True
      c.append(escolha_Q14)
      questao_15()
      return escolha_Q14
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()

def questao_15():
  proxima_pergunta = False
  while proxima_pergunta == False:
    formatacao.forma_linha()
    print(mensagens.perguntas[14].upper())
    mensagens.opcoes()
    escolha_Q15 = int(input('Escolha uma das opções acima (1, 2, 3, 4 ou 5): '))
    if escolha_Q15 == 1 or escolha_Q15 == 2 or escolha_Q15 == 3 or escolha_Q15 == 4 or escolha_Q15 == 5:
      clear()
      proxima_pergunta = True
      formatacao.forma_linha()
      c.append(escolha_Q15)
      print(' SEGUE O RESULTADO DO QUIZ: '.center(80))
      return escolha_Q15
    else:
      texto_alerta = 'Digite somente 1, 2, 3, 4 ou 5! '
      texto_continua = 'Digite qualquer coisa para continuar:'
      print(formatacao.escolher_cor('yellow', texto_alerta))
      continua = input(formatacao.escolher_cor('green', texto_continua))
      if continua != 1 or continua != 2 or continua != 3 or continua != 4 or continua != 5:
        proxima_pergunta = False
        clear()