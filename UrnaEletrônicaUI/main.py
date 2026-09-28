from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import QTimer
from urna import *
from candidato import *
from playsound3 import playsound
import sys
empate = bool



def botaonumero(numero):

    numeroAtual = janela.numeroPrint.text()

    if len(numeroAtual) < 2:
        janela.numeroPrint.setText(f"{numeroAtual}{numero}") 

    numeroAtual = janela.numeroPrint.text()

def botaocorrige():
    
    numeroAtual = janela.numeroPrint.text()
    novoNumero = numeroAtual[:-1]
    janela.numeroPrint.setText(f"{novoNumero}")

def botaoconfirma():

    for candidato in listaCandidatos:
        
        if int(janela.numeroPrint.text()) == candidato.numero:
            candidato.quantVotos +=1
            sound = playsound("C:/Users/Grizenti/Downloads/pirirililili (mp3cut.net).mp3", block=False)

            break #dói no coração lembrar daqueles que se foram 

    else: 
        textoinvalido = janela.mensagemVoto.setText("Voto Inválido! 😑")
        
def botaoencerrar():
    global vencedores
    vencedores = []

    maisVotos = max(candidato.quantVotos for candidato in listaCandidatos)
        
    for candidato in listaCandidatos:
        if candidato.quantVotos == maisVotos:
            vencedores.append(candidato)
        if len(vencedores) == 1:
            vencedor = vencedores[0]
            janela.mensagemVoto.setText(f'O(a) vencedor(a) da eleição foi o(a) candidato(a) {vencedor.nome} com {vencedor.quantVotos} votos!')
            
    


app = QtWidgets.QApplication([])

janela = uic.loadUi("tse.ui") # tela do qtDesign


janela.bt1.clicked.connect(lambda: botaonumero(1))#///botões com numeros
janela.bt2.clicked.connect(lambda: botaonumero(2))
janela.bt3.clicked.connect(lambda: botaonumero(3))
janela.bt4.clicked.connect(lambda: botaonumero(4))
janela.bt5.clicked.connect(lambda: botaonumero(5))
janela.bt6.clicked.connect(lambda: botaonumero(6))
janela.bt7.clicked.connect(lambda: botaonumero(7))
janela.bt8.clicked.connect(lambda: botaonumero(8))
janela.bt9.clicked.connect(lambda: botaonumero(9))
janela.bt0.clicked.connect(lambda: botaonumero(0))#\\\
janela.btCorrige.clicked.connect(botaocorrige)
janela.btConfirma.clicked.connect(botaoconfirma)
janela.btEncerrar.clicked.connect(botaoencerrar)

janela.show()
app.exec()