
from tkinter import *
import os
import pyautogui as pg
import design_de_software
import matematica_dif
import programacao_ex

def semNome():
    print('')

app = Tk()
app.title('Matérias da Faculdade')

app.geometry('600x600')
bg = PhotoImage()
app.resizable(width=0, height=0)

menubar = Menu(app)
#design de software menu
mds = Menu(menubar, tearoff=0)
mds.add_command(label='Evolução dos Sistemas Computacionais', command=design_de_software.esc)
mds.add_command(label='Detalhamento das Etapas de Projeto', command=design_de_software.dep)
mds.add_command(label='Detalhamento do Ciclo de Vida', command=design_de_software.dcv)
mds.add_command(label='Tipos de Processos e Requisitos', command=design_de_software.tpr)
mds.add_command(label='Desenvolvimento de Escopo...', command=design_de_software.dema)
mds.add_command(label='Conceituação e Aplicação dos Diagramas', command=design_de_software.cad)
mds.add_command(label='Atividades e Casos de Uso', command=design_de_software.acu)
mds.add_command(label='Classes, Componentes e Objetos', command=design_de_software.cco)
mds.add_command(label='Sequência, Colaboração e Tempo', command=design_de_software.sct)
mds.add_command(label='Estrtutura e Comportamento', command=design_de_software.ec)
mds.add_command(label='Instalação e Pacote', command=design_de_software.ip)
mds.add_command(label='Interação, Interatividade e Máquina', command=design_de_software.iim)
mds.add_command(label='Revisão e Conceituação de O.O', command=design_de_software.rco)
mds.add_command(label='Programação de UML em O.O', command=design_de_software.puo)
mds.add_command(label='Descrição e Diferenciação de Mapeamentos', command=design_de_software.ddm)
mds.add_command(label='Projeto de Software', command=design_de_software.ps)
menubar.add_cascade(label='Design de Software',menu=mds)

#Matemática Diferencial Aplicada Menu
menuMDA = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Matemática Diferencial Aplicada',menu=menuMDA)
menuMDA.add_command(label='Conjuntos Numéricos', command=matematica_dif.cj)
menuMDA.add_command(label='Conceitos e Definições de Funções', command=matematica_dif.cdf)
menuMDA.add_command(label='Funções Importantes', command=matematica_dif.fi)
menuMDA.add_command(label='Funções Elementares', command=matematica_dif.fe)
menuMDA.add_command(label='Noção de Limite de uma Função', command=matematica_dif.nlf)
menuMDA.add_command(label='Limites Indeterminados', command=matematica_dif.li)
menuMDA.add_command(label='Limites Indeterminados - Aplicação', command=matematica_dif.lia)
menuMDA.add_command(label='Continuidade', command=matematica_dif.cn)
menuMDA.add_command(label='A Reta Tangente', command=matematica_dif.art)
menuMDA.add_command(label='Deriváveis', command=matematica_dif.de)
menuMDA.add_command(label='Derivadas Elementares', command=matematica_dif.delem)
menuMDA.add_command(label='Derivadas Aplicadas', command=matematica_dif.da)
menuMDA.add_command(label='Acréscimos e Diferenciais', command=matematica_dif.cj)
menuMDA.add_command(label='Teoremas e Funções', command=matematica_dif.cj)
menuMDA.add_command(label='Extremos, Concavidade e Inflexão', command=matematica_dif.cj)
menuMDA.add_command(label='Regras de Derivação', command=matematica_dif.cj)


#Programação Extrema Menu
menuPEX = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Programação Extrema',menu=menuPEX)
menuPEX.add_command(label='Escrever aqui a aula', command=semNome)


app.config(menu=menubar)
app.mainloop()