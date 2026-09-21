from cores import *
class Candidatos:

    def __init__(self, nome, partido, numero, quantVotos,):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.quantVotos = quantVotos
    
    def exibirCandidato(self):
        return ' {}  |   {}   |  {} '.format(self.nome, self.partido, self.numero)

    def votar(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo):
        print(f'Muito bem, eleitor, agora você deve votar, pois nesse país, {vermelho}todos{reset} são obrigados a tal')
        print()
        tabelaGeral(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo)
        print()
        print(f'Digite o número de um candidato')

        listaCandidatos = [
        candidato1,
        candidato2,
        candidato3,
        candidato4,
        candidato5,
        candidatoNulo
    ]
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
                    else:
                        print(f'{vermelho}Voto inválido{reset}')
                        espaço()

        listaQuantVotos = [

        candidato1.quantVotos,
        candidato2.quantVotos,
        candidato3.quantVotos,
        candidato4.quantVotos,
        candidato5.quantVotos,
        candidatoNulo.quantVotos
    ]
        maisVotos = max(listaQuantVotos)
        print(maisVotos)

        
def espaço():
    print('')
    print('------------------------')
    print('')

def tabelaGeral( candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo ):
        print(' Nome   Partido  Número')
        print(candidato1.exibirCandidato())
        print(candidato2.exibirCandidato())
        print(candidato3.exibirCandidato())
        print(candidato4.exibirCandidato())
        print(candidato5.exibirCandidato())
        print(candidatoNulo.exibirCandidato())