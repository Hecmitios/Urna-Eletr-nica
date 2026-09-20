from cores import *
class Candidatos:

    def __init__(self, nome, partido, numero, numeroVotos,):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.numeroVotos = numeroVotos
    
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

        voto = int(input(''))

        for candidato in listaCandidatos:
            if voto == candidato.numero:
                print('Confirma?')
                print(f'{verde}s{reset} {amarelo}OU{reset} {vermelho}n{reset}')

                confirmar = input('').lower()

                if confirmar == 's':
                    candidato.numeroVotos += 1
                    print(f'{verde}Voto {negrito}confirmado!{reset}{reset}')

                elif confirmar == 'n':
                    print(f'{vermelho}Voto {negrito}cancelado{reset}{reset}.')

                else:
                    print(f'{vermelho}Voto {negrito}inválido{reset}{reset}')

        
        

def tabelaGeral( candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo ):
        print(' Nome   Partido  Número')
        print(candidato1.exibirCandidato())
        print(candidato2.exibirCandidato())
        print(candidato3.exibirCandidato())
        print(candidato4.exibirCandidato())
        print(candidato5.exibirCandidato())
        print(candidatoNulo.exibirCandidato())