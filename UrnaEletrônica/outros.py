#Este é um arquivo onde tomei a liberdade de colocar funções mais bobas e estéticas, tais como as cores
from playsound3 import playsound

preto = '\033[1;30m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
magenta = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;37m'
cinza = '\033[1;90m'
negrito = '\033[1m'
reset = '\033[0m'

empate = bool


#emojis aí ó
envergonhado = '\U0001F633' # 😳
assustado =  "\U0001F631"  # 😱
surpreso =    "\U0001F632"  # 😲
bocaFechada = "\U0001F910"  # 🤐
pensativo =      "\U0001F914"  # 🤔
neutro =         "\U0001F610"  # 😐
semExpressão = "\U0001F611" # 😑


def espaço(cor): 
        print('')
        print(f'{cor}_{reset}'*30)
        print('')



def tabelaGeral(listaCandidatos):
            
            print(' Nome   Partido  Número')
            for candidato in listaCandidatos:
                print(candidato.exibirCandidato())

