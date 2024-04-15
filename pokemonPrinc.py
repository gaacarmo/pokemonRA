#importando biblioteca randomica
import random

#criando listas e variaveis
pokemons_caverna=['Onix','Zubat','Diglet','Geodude']
pokemons_mato=['Bulbasaur','Caterpie','Bellsprout','Abra']
pokedex=[]
tentativas = 3
    
#introdução professor carvalho, e escolha de um nome para o jogador
print(f"*professor carvalho aparece*")
nomeJogador = input(f"Professor Carvalho - olá treinador, bem vindo ao mundo Pokemón. Eu sou o professor Carvalho, como posso te chamar? \nDigite aqui seu nome: ")
print(f"Professor carvalho - É um prazer te conhecer, {nomeJogador}. Esta é a cidade de Pallet, da região de Kanto!\n")
    
    #escolha do bioma
for i in range(0,10):  
    escolha=int(input("Escolha para onde deseja ir\n1. Ir para a Floresta\n2. Ir para a Caverna\n3. Abrir Pokedex\n4. Sair\n:"))
    
    #checkando validade de escolha
    if escolha >4 or escolha<0:
        print("\nNão foi possível encontrar alguma função com este número digitado!\n")
        
    #criando  a escolha do bioma da Floresta
    if escolha == 1:
        
        #escolha randomica do pokemon que o jogador vai encontrar na floresta!
        pok = random.choice(pokemons_mato)
        print(f"Você entrou na Floresta e encontou um {pok}\n")
        #escolha do jogador se ele vai ou nao querer capturar o pokemon
        captura = input("Você deseja capturar este pokemon? (s/n): \n")
        
        #checagem de escolha
        if captura != "s" or captura != "n": #aqui ta bugado kk
            print('tente novamente com uma opção válida')
        
        #caso o jogador escolha capturar: 
        if captura == 's':
             #sorteio se o jogador ira ou não capturar com uma probabilidade de captura de 50%
             num1 = random.randint(0,1)
             num2 = random.randint(0,1)
             if num1 == num2:
                print(f"Você capturou o {pok}\n") #caso haja a captura
                pokedex.append(i)
             else:
                nova = input('Voce nao consegui capturar o pokemon!\nDeseja tentar capturar novamente? (s/n) ') #caso não haja captura e o usuarrio recebe novas opções
               
                if nova != 's':
                    print(f'Voce capturou o {pok}!\n' ) #caso haja captura na segunda tentativa
                    tentativas -= 1
                    #ele não deveria dar um append aqui?
                  
                    if nova == 's':
                        print(f"Você capturou o {pok}\n") 
                        pokedex.append(pok)
                    elif nova == 'n':
                        print(f"Ok, você escolheu não capturar o {pok}.\n")  
                elif captura == 'n':
                    print(f"Ok, você escolheu não capturar o {pok}.")  
        
    #caso a escolha seja a da carverna
    if escolha == 2:
        
        #escolha randomica de pokemons encontrados na caverna
        pok = random.choice(pokemons_caverna)
        print(f"Você entrou na caverna e encontou um {pok}\n")
        #escolha de captura
        captura = input("Você deseja capturar este pokemon? (s/n): \n")
        
        #checagem da escolha de captura
        if captura != "s" or captura != "n":
            print('tente novamente com uma opção válida')
        
        #caso o jogador queira tentar capturar
        if captura == 's':
             
             #sorteando a chance de 50% da captura do pokemon
             num1= random.randint(0,1)
             num2= random.randint(0,1)
             if num1 == num2: #caso haja captura
                print(f"Você capturou o {pok}\n")
                pokedex.append(i)
             else:
                nova=input('Voce nao consegui capturar o pokemon!\nDeseja tentar capturar novamente? (s/n) ') #caso não haja captura e escolha
                if nova != 's':
                    print(f'Voce capturou o {pok}!\n' )
                    tentativas-=1
                  
                    if nova == 's':
                        print(f"Você capturou o {pok}\n")
                        pokedex.append(pok)
                    elif nova == 'n':
                        print(f"Ok, você escolheu não capturar o {pok}.\n")  
                elif captura == 'n':
                    print(f"Ok, você escolheu não capturar o {pok}.")
    if escolha == 3:
        print(f"aqui são todos os pokemons que você ja capturou {pokedex}") # aqui temos outro bug kkkk, ele mostra o indice do pokemon ao inves do pokemon
    if escolha == 4:
        print("Até logo!")
        break