from candidato import *

class Urna:

    def __init__(Candidato, nome, partido, numero, quantVotos,):
            Candidato.nome = nome
            Candidato.partido = partido
            Candidato.numero = numero
            Candidato.quantVotos = quantVotos

    def apresentacao(listaCandidatos):

        print(f'Muito bem, eleitor, agora você deve votar, pois nesse país, {vermelho}todos{reset} são obrigados a tal {pensativo}')
        espaço(negrito)
        tabelaGeral(listaCandidatos) #tabela com os candidatos e numeros
        espaço(negrito)
    
    def votar(listaCandidatos):

        for i in range (5): #Votação de facto
            voto = int(input('Vote: '))
    
            for candidato in listaCandidatos:


                if voto == candidato.numero:
                    print(f'Confirma seu voto no(a) candidato(a) {candidato.nome}?')
                    print(f'{verde}s{reset} {amarelo}OU{reset} {vermelho}n{reset}')
    
                    confirmar = input('').lower()
    
                    if confirmar == 's':
                        candidato.quantVotos += 1
                        print(f'{verde}Voto confirmado!{reset}')
                        sound = playsound("C:/Users/Grizenti/Downloads/pirirililili (mp3cut.net).mp3", block=False)
                        espaço(negrito)
                        
                    elif confirmar == 'n':
                        print(f'{vermelho}Voto cancelado{reset}.')
                        espaço(negrito)
                    break
            else:
                
                print(f'{vermelho}Voto inválido{reset}')
                espaço(branco)

    def apurar(listaCandidatos):
            global vencedores
            vencedores = []
            maisVotos = max(candidato.quantVotos for candidato in listaCandidatos)

            for candidato in listaCandidatos:
                if candidato.quantVotos == maisVotos:
                    vencedores.append(candidato)
            if len(vencedores) == 1:
                vencedor = vencedores[0]
                print(f'O(a) candidato(a) {vencedor.nome} {verde}venceu{reset} a eleição com {verde}{vencedor.quantVotos}{reset} votos ao todo!')  
            else:
                
                print(f'Deu {cinza}empate!{reset}{surpreso}')
                print()
                global empate 
                empate = True
    
    def segundoTurno(self):
        if empate == True:
            
            print('Então vamos começar esse segundo turno!')
            print('Vote nos candidatos ainda em disputa. São eles:')
            espaço(negrito)
            tabelaGeral(vencedores)
            espaço(negrito)

            print(f'{vermelho}Agora vamos decidir isso.{reset}')

            self.votar(vencedores)
            self.apurar(vencedores)


                    