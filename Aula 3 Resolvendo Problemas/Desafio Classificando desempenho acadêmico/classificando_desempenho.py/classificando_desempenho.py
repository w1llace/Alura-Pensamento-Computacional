'''
Você está trabalhando no desenvolvimento de um sistema educacional que precisa 
exibir mensagens personalizadas para estudantes com base em sua média final. A regra de negócio 
definida pela equipe pedagógica é a seguinte:

Média menor que 5,0: mensagem “Você está reprovado.”
Média entre 5,0 e 6,9: mensagem “Você está de recuperação.”
Média 7,0 ou mais: mensagem “Parabéns! Você foi aprovado.”

Sua tarefa é criar um algoritmo em linguagem natural que represente esse processo de verificação
e decisão de forma clara, usando estruturas condicionais.'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

def media(nota1, nota2):

    media_final = (nota1 + nota2) / 2


    if media_final < 5.0:
        return print("\nVocê está reprovado.")

    elif 5.0 <= media_final < 7.0:
        return print("\nVocê está de recuperação.")

    else:
        return print("\nParabéns! Você foi aprovado.")

#chamando a função para calcular a média e exibir a mensagem correspondente
media(nota1, nota2)