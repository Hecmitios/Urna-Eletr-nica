from urna import * 


class JanelaUrna(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        
        uic.loadUi("tse.ui", self)
        self.setWindowTitle("Urna")
        self.setWindowIcon(QIcon("imagens/urnalogo.png"))

        
        self.bt1.clicked.connect(lambda: self.botaonumero(1))
        self.bt2.clicked.connect(lambda: self.botaonumero(2))
        self.bt3.clicked.connect(lambda: self.botaonumero(3))
        self.bt4.clicked.connect(lambda: self.botaonumero(4))
        self.bt5.clicked.connect(lambda: self.botaonumero(5))
        self.bt6.clicked.connect(lambda: self.botaonumero(6))
        self.bt7.clicked.connect(lambda: self.botaonumero(7))
        self.bt8.clicked.connect(lambda: self.botaonumero(8))
        self.bt9.clicked.connect(lambda: self.botaonumero(9))
        self.bt0.clicked.connect(lambda: self.botaonumero(0))
        self.btCorrige.clicked.connect(self.botaocorrige)

        
        self.btConfirma.clicked.connect(lambda: self.botaoconfirma(listaCandidatos))
        self.btEncerrar.clicked.connect(lambda: self.botaoencerrar(listaCandidatos))
        


    
    def botaonumero(self, numero): 
        numeroAtual = self.numeroPrint.text()

        if len(numeroAtual) < 2:
            self.numeroPrint.setText(f"{numeroAtual}{numero}") 

    def botaocorrige(self):
        numeroAtual = self.numeroPrint.text()
        novoNumero = numeroAtual[:-1]
        self.numeroPrint.setText(f"{novoNumero}")

    def botaoconfirma(self, listadomomento):
        Urna.votar(self, listadomomento) 

    def botaoencerrar(self, listadomomento):
        Urna.apurar(self, listadomomento)

        global encerramento
        encerramento = True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_principal = JanelaUrna()
    janela_principal.show()
    sys.exit(app.exec())