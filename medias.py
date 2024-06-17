alunos = {}

def menu():
    print('1 - adicionar aluno')
    print('2 - listar aluno')
    print('3 - remover aluno')
    print('4 - procurar aluno')
    print('5 - aprovados')
    print('6 - reprovados')
    print('7 - procurar pelo nome do aluno')
    print('8 - média da turma B1')
    print('9 - Média da turma B2')
    print('10 - Média da turma GERAL')
    print('11 - Diario do aluno')
    print('0 - sair')

    try:
           opt = int(input('digite a opção: '))
           return opt
    except Exception as e:
         print(f"opcao invalida: {e}")
         return 9
    
def add_aluno():
    try:
        ra = input('Digite o RA do aluno: ')
        nome = input('Digite o nome do aluno: ')
        nota_b1 = float(input('Digite a nota B1 do aluno: '))
        nota_b2 = float(input('Digite a nota B2 do aluno: '))
        media = (nota_b1 + nota_b2) / 2
        dados = {"nome": nome, 'b1': nota_b1, 'b2': nota_b2, 'media': media}  
        alunos[ra] = dados
    except Exception as e:
        print(f"Erro ao adicionar aluno: {e}")


def listar_alunos():
     for ra, dados in alunos.items():
          print(f'RA: {ra} - aluno: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}')
          input('pressione qualquer tecla para continuar')

def remover_aluno():
    ra = input('digite o RA do aluno:')
    if ra in alunos:
         aluno = alunos.pop(ra)
         print(f'o aluno: {aluno['nome']} foi removido')
    else:
         print('o aluno nao encontrado!')
         input('pressione qualquer tecla para continuar')

def procurar_alunos():
      ra = input('digite o RA do aluno: ')
      if ra in alunos:
          dados = alunos[ra]
          print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
          media = (dados['b1'] + dados['b2']) / 2
          print(f"Média: {media}")
      else:
          print("aluno nao encontrado!")
          input('pressione qualquer tecla para continuar')
 
def aprovados():
     for ra, dados in alunos.items():
        media = (dados['b1'] + dados['b2']) / 2
        if media >= 7:
            print(f"RA: {ra} - Nome: {dados['nome']} - Média: {media}")
     return      

def reprovados():
     for ra, dados in alunos.items():
        media = (dados['b1'] + dados['b2']) / 2
        if media < 7:
            print(f"RA: {ra} - Nome: {dados['nome']} - Média: {media}")
     return  


def nome_aluno():
    nome = input('Digite o nome do aluno: ')
    for ra, dados in alunos.items():
        if dados['nome'] == nome:
            print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
            break
    else:
        print("Aluno não encontrado!")
    input('Pressione qualquer tecla para continuar...')




def mediaTurB1():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b1']
        qtd += 1
        media = soma / qtd
        print(f'a media da b1 é:{media:.2f}')
        input('pressione qualquer tecla para continuar')






def mediaTurB2():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b2']
        qtd += 1
        media = soma / qtd
        print(f'a media da b2 é:{media:.2f}')
        input('pressione qualquer tecla para continuar')

     


def mediaTurGeral():
    total_notas = 0
    total_alunos = 0
    for dados in alunos.values():
        total_notas += dados['b1'] + dados['b2']
        total_alunos += 1

    if total_alunos == 0:
        print("Não há alunos na turma.")
    else:
        media_geral = total_notas / (total_alunos * 2)  
        print(f"A média geral da turma é: {media_geral:.2f}")
    input('Pressione qualquer tecla para continuar...')



def Diario_aluno():
    linha = '-' * 56
    print(" " * 20 + "Diario da turma")
    print(linha)
    print('| RA    | Nome                      | Nota B1  | Nota B2  | Média  |')
    print(linha)

    for ra, dados in alunos.items():
        ra_formatado = ra.ljust(5)
        nome = dados['nome'].ljust(27)
        b1 = f"{dados['b1']:.2f}".rjust(5)
        b2 = f"{dados['b2']:.2f}".rjust(5)
        media = f"{dados['media']:.2f}".rjust(5)
        print(f'| {ra_formatado} | {nome} | {b1} | {b2} | {media} |')
    print(linha)

   
    media_b1_turma = sum(dados['b1'] for dados in alunos.values()) / len(alunos)
    media_b2_turma = sum(dados['b2'] for dados in alunos.values()) / len(alunos)
    media_geral_turma = sum(dados['media'] for dados in alunos.values()) / len(alunos)
    
    print("|" + "-" * 56 + "|")
    print(f"|{'Médias da Turma'.center(56)}|")
    print("|" + "-" * 56 + "|")
    print(f"|{'':<35} | {media_b1_turma:.2f} | {media_b2_turma:.2f} | {media_geral_turma:.2f} |")
    print("|" + "-" * 56 + "|")

     
   

if __name__ == '__main__':
    while True:
         match menu():
              case 1:
                   add_aluno()
              case 2:
                   listar_alunos()                   
              case 3:
                   remover_aluno()
              case 4:
                   procurar_alunos()
              case 5:
                   aprovados()
              case 6:
                   reprovados()
              case 7:
                   nome_aluno()
              case 8:
                   mediaTurB1()
              case 9:
                   mediaTurB2()
              case 10:
                   mediaTurGeral()   
              case 11:
                   Diario_aluno()               
              case 0:
                   break   
                       
