from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6 import uic, QtWidgets
from playsound3 import playsound
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap, QIcon
from candidato import *
import sys
import os

class Urna:

    @staticmethod
    def votar(JanelaUrna, lista):

        for candidato in lista:
            
            if str(JanelaUrna.numeroPrint.text()) == (candidato.numero):
                candidato.quantVotos +=1

                urnaSom = playsound('audio/urna_som.mp3', block = False) 
                JanelaUrna.mensagemVoto.setText('Voto confirmado!') 
                QTimer.singleShot(1000, lambda:JanelaUrna.numeroPrint.setText('')) 
                QTimer.singleShot(1200, lambda:JanelaUrna.mensagemVoto.setText('')) 
                
                break 
    
        else: 
            textoinvalido = JanelaUrna.mensagemVoto.setText("Voto Inválido! 😑")
            JanelaUrna.numeroPrint.setText('') 
            QTimer.singleShot(1000, lambda: JanelaUrna.mensagemVoto.setText(''))
            
            
              
    
    def apurar(JanelaUrna, lista):
            
            global vencedores
            vencedores = []
            
            maisVotos = max(candidato.quantVotos for candidato in lista)
                    
            for candidato in lista:

                if candidato.quantVotos == maisVotos:
                    vencedores.append(candidato)

            if len(vencedores) == 1:
                JanelaUrna.numeroPrint.setText((str()))
                vencedor = vencedores[0]
                
                if vencedor.nome == 'NULO':
                    JanelaUrna.mensagemVoto.setText('VOTAÇÃO ADIADA, O NULO GANHOU')
                    
                else:
                    JanelaUrna.mensagemVoto.setText('VENCEDOR(a)')
                
                imagemVencedor = QPixmap(vencedor.imagem)
                JanelaUrna.imagemCandidato.setPixmap(imagemVencedor)

                QTimer.singleShot(5000, JanelaUrna.close)
                    

            else:

                if candidatoNulo not in (vencedores): vencedores.append(candidatoNulo)
                for candidato in listaCandidatos: candidato.quantVotos = 0

                JanelaUrna.listaAtual = vencedores
                JanelaUrna.turnoAtual +=1
                JanelaUrna.setWindowTitle(f'Urna - {JanelaUrna.turnoAtual}º turno')
                
                JanelaUrna.mensagemVoto.setText('Deu empate!')
                QTimer.singleShot(2000, lambda: JanelaUrna.mensagemVoto.setText(f'{JanelaUrna.turnoAtual}º turno!'))
                QTimer.singleShot(2000, lambda: JanelaUrna.mensagemVoto.setText(''))
                JanelaUrna.imagemCandidato.clear()

                global segundo_turno
                segundo_turno = True

                

    
    
        
        

            


