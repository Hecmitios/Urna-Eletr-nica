from candidato import *

class Urna:

    def __init__(Candidato, nome, partido, numero, quantVotos,):
            Candidato.nome = nome
            Candidato.partido = partido
            Candidato.numero = numero
            Candidato.quantVotos = quantVotos
    
    def votar(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo):


        listaCandidatos = [
                                candidato1,
                                candidato2,
                                candidato3,
                                candidato4,
                                candidato5,
                                candidatoNulo
                                ]
        
        print(f'Muito bem, eleitor, agora você deve votar, pois nesse país, {vermelho}todos{reset} são obrigados a tal')
        print()
        tabelaGeral(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo)
        print()
        print(f'Digite o número de um candidato')

    
        for i in range (5):
            voto = int(input('Vote: '))
    
            for candidato in listaCandidatos:


                if voto == candidato.numero:
                    print(f'Confirma seu voto no(a) candidato(a) {candidato.nome}?')
                    print(f'{verde}s{reset} {amarelo}OU{reset} {vermelho}n{reset}')
    
                    confirmar = input('').lower()
    
                    if confirmar == 's':
                        candidato.quantVotos += 1
                        print(f'{verde}Voto confirmado!{reset}')
                        espaço()
                    elif confirmar == 'n':
                        print(f'{vermelho}Voto cancelado{reset}.')
                        espaço()
                    break
            else:
                
                print(f'{vermelho}Voto inválido{reset}')
                espaço()
    def apurar(listaCandidatos):
    
    
            maisVotos = max(candidato.quantVotos for candidato in listaCandidatos)
            for candidato in listaCandidatos:
                if candidato.quantVotos == maisVotos:
                    print(f'O(a) candidato (a) {candidato.nome} {verde}venceu{reset} a eleição com {verde}{candidato.quantVotos}{verde} votos!')               
    
    
            
def espaço():
        print('')
        print('------------------------')
        print('')

def tabelaGeral(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo ):
            
            print(' Nome   Partido  Número')
            print(candidato1.exibirCandidato())
            print(candidato2.exibirCandidato())
            print(candidato3.exibirCandidato())
            print(candidato4.exibirCandidato())
            print(candidato5.exibirCandidato())
            print(candidatoNulo.exibirCandidato())