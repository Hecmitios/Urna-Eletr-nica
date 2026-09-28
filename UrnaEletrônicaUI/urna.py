from candidato import *

class Urna:
    
    def votar(listaCandidatos):

        for i in range (5): #Votação de facto
            voto = int(input('Vote: '))
    
            for candidato in listaCandidatos:


                if voto == candidato.numero:
    
                    confirmar = input('').lower()
    
                    if confirmar == 's':
                        candidato.quantVotos += 1
                        print('Voto confirmado!')
                        
                        
                    elif confirmar == 'n':
                        print(f'Voto cancelado.')
                    break
            else:
                
                print('Voto inválido')

    def apurar(listaCandidatos):
            global vencedores
            vencedores = []
            maisVotos = max(candidato.quantVotos for candidato in listaCandidatos)

            for candidato in listaCandidatos:
                if candidato.quantVotos == maisVotos:
                    vencedores.append(candidato)
            if len(vencedores) == 1:
                vencedor = vencedores[0]
                print(f'O(a) candidato(a) {vencedor.nome} venceu a eleição com {vencedor.quantVotos}votos ao todo!')  
            else:
                
                print(f'Deu empate!')
                print()
                global empate 
                empate = True

    def apurar2(listaCandidatos):
                global vencedores
                vencedores = []
                maisVotos = max(candidato.quantVotos for candidato in listaCandidatos)
    
                for candidato in listaCandidatos:
                    if candidato.quantVotos == maisVotos:
                        vencedores.append(candidato)
                if len(vencedores) == 1:
                    vencedor = vencedores[0]
                    
                else:
                    
                    print('Deu empate!')
                    print()
                    global empate 
                    empate = True
    
    def segundoTurno(self):
        if empate == True:
            
            print('Então vamos começar esse segundo turno!')
            print('Vote nos candidatos ainda em disputa. São eles:')

            print(f'Agora vamos decidir isso.')

            self.votar(vencedores)
            self.apurar(vencedores)


