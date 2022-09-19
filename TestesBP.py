from functions.func_cana import cana_de_acucar
from functions.func_milho import milho
from functions.func_soja import soja




def menu():
    opcao = input(''' Digite o nome da espécie desejada 
    [1] Soja
    [2] Cana
    [3] Milho
    ''')

    if opcao == '1':
        soja()

    elif opcao == '2':
        cana_de_acucar()
    
    elif opcao == '3':
        milho()
    
    



def main():
    menu()
main()
