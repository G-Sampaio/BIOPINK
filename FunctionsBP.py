#---------------------------------------------------------------------------------------------
#CANA DE ACUCAR
#---------------------------------------------------------------------------------------------
def cana_de_acucar():
    opcao_escolha_cana = input('''Selecione 
    [1] 16S
    [2] ITS 
    ''')

    opcao_escolha_cana2 = input('''Selecione Cultura
    [1] Cultura 1
    [2] Cultura 2
    [3] Cultura 3
    ''')
    opcao_escolha_cana3 = input('''Selecione Região
    [1] Brasil
    [2] América do sul
    [3] Mundo
    ''')

    if opcao_escolha_cana == '1':
        escolha = '((escolha_cana>AND>16S'
        print("você optou por 16S")
    
    elif opcao_escolha_cana == '2':
        escolha = '((escolha_cana>AND>ITS'
        print("Você optou por ITS")

    
    if opcao_escolha_cana2 == '1':
        cultura_cana = '>AND>Cultura1'
        print('Você selecionou a cultura 1!')
    
    elif opcao_escolha_cana2 == '2':
        cultura_cana = '>AND>Cultura2'
        print('Você selecionou a cultura 2!')
    
    elif opcao_escolha_cana2 == '3':
        cultura_cana = '>AND>Cultura3'
        print('Você selecionou a cultura 3!')


    if opcao_escolha_cana3 == '1':
        regiao_cana = '>AND>regiao_Brasil))' 
        print('Você selecionou a região: Brasil')
    
    elif opcao_escolha_cana3 == '2':
        regiao_cana = '>AND>regiao_America_do_sul))' 
        print('Você selecionou a região: América do sul')
    
    elif opcao_escolha_cana3 == '3':
        regiao_cana = '>AND>regiao_Mundo))' 
        print('Você selecionou a região: Mundo')
        
    print(escolha+cultura_cana+regiao_cana)
#-----------------------------------------------------
#Milho
#-----------------------------------------------------

def milho():
    opcao_escolha_milho = input('''Selecione 
    [1] 16S
    [2] ITS 
    ''')

    opcao_escolha_milho2 = input('''Selecione Cultura
    [1] Cultura 1
    [2] Cultura 2
    [3] Cultura 3
    ''')
    opcao_escolha_milho3 = input('''Selecione Localização
    [1] Brasil
    [2] América do sul
    [3] Mundo
    ''')

    if opcao_escolha_milho == '1':
        escolha = '((escolha_milho>AND>16S'
        print("você optou por 16S")
    
    elif opcao_escolha_milho == '2':
        escolha = '((escolha_milho>AND>ITS'
        print("Você optou por ITS")

    
    if opcao_escolha_milho2 == '1':
        cultura_milho = '>AND>Cultura1'
        print('Você selecionou a cultura 1!')
    
    elif opcao_escolha_milho2 == '2':
        cultura_milho = '>AND>Cultura2'
        print('Você selecionou a cultura 2!')
    
    elif opcao_escolha_milho2 == '3':
        cultura_milho = '>AND>Cultura2'
        print('Você selecionou a cultura 3!')


    
    if opcao_escolha_milho3 == '1':
        regiao_milho = '>AND>regiao_Brasil))' 
        print('Você selecionou a região: Brasil')
    
    elif opcao_escolha_milho3 == '2':
        regiao_milho = '>AND>regiao_America_do_sul))' 
        print('Você selecionou a região: América do sul')
    
    elif opcao_escolha_milho3 == '3':
        regiao_milho = '>AND>regiao_Mundo))' 
        print('Você selecionou a região: Mundo')
        
    print(escolha+cultura_milho+regiao_milho)
#------------------------------------------------------------
#SOJA
#------------------------------------------------------------


def soja():
    opcao_escolha_soja = input('''Selecione 
    [1] 16S
    [2] ITS 
    ''')

    opcao_escolha_soja2 = input('''Selecione Cultura
    [1] Cultura 1
    [2] Cultura 2
    [3] Cultura 3
    ''')
    opcao_escolha_soja3 = input('''Selecione Localização
    [1] Brasil
    [2] América do sul
    [3] Mundo
    ''')

    if opcao_escolha_soja == '1':
        escolha = '((escolha_soja>AND>16S'
        print("você optou por 16S")   
    elif opcao_escolha_soja == '2':
        escolha = '((escolha_soja>AND>ITS'
        print("Você optou por ITS")

    
    if opcao_escolha_soja2 == '1':
        cultura_soja = '>AND>Cultura1'
        print('Você selecionou a cultura 1!')  
    elif opcao_escolha_soja2 == '2':
        cultura_soja = '>AND>Cultura2'
        print('Você selecionou a cultura 2!')   
    elif opcao_escolha_soja2 == '3':
        cultura_soja = '>AND>Cultura2'
        print('Você selecionou a cultura 3!')


    if opcao_escolha_soja3 == '1':
        regiao_soja = '>AND>regiao_Brasil))' 
        print('Você selecionou a região: Brasil')  
    elif opcao_escolha_soja3 == '2':
        regiao_soja = '>AND>regiao_America_do_sul))' 
        print('Você selecionou a região: América do sul')   
    elif opcao_escolha_soja3 == '3':
        regiao_soja = '>AND>regiao_Mundo))' 
        print('Você selecionou a região: Mundo')
    
    print(escolha+cultura_soja+regiao_soja)
