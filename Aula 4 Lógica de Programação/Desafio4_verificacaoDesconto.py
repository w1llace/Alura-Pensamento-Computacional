'''
Você está desenvolvendo o sistema de bilheteria para um cinema. Os clientes podem ter 
direito a meia-entrada em duas situações:

Se tiverem menos de 18 anos

ou

Se forem estudantes

Sua tarefa é criar um algoritmo em linguagem natural ou gráfica (usando fluxogramas, por exemplo) que 
avalie as informações do cliente e exiba uma mensagem indicando se ele tem ou não direito ao desconto.
'''

cliente_idade = 25

cliente_estudante = False

if cliente_idade < 18 or cliente_estudante:
    print("O cliente tem direito à meia-entrada.")
else:
    print("O cliente não tem direito à meia-entrada.")
