from re import M
from FunctionsBP import cana_de_acucar
from FunctionsBP import milho
from FunctionsBP import soja



def menu():
    opcao = input(''' Digite o nome da espécie desejada 
    [1] Soja
    [2] Cana
    [3] Milho
    ''')

    if opcao == '1':
        soja

    if opcao == '2':
        cana_de_acucar
    
    if opcao == '3':
        FunctionsBP.milho
    
    



def main():
    menu()
main()
