#importando biblioteca randomica
import random

#criando listas e variaveis
pokemonsIniciais = ["Bulbasaur","Squirtle","Charmander"]
pokemons_caverna=['Onix','Zubat','Diglet','Geodude']
pokemons_mato=['Bulbasaur','Caterpie','Bellsprout','Abra']
rep_floresta=[]
rep_caverna=[]
pokedex=[]
tentativas = 3
    
#introdução professor carvalho, e escolha de um nome para o jogador
print(f"professor carvalho aparece")
nomeJogador = input(f"Professor Carvalho - olá treinador, bem vindo ao mundo Pokemón. Eu sou o professor Carvalho, como posso te chamar? \nDigite aqui seu nome: ")
print(f"\nProfessor carvalho - É um prazer te conhecer, {nomeJogador}. Esta é a cidade de Pallet, da região de Kanto!\n")

#escolhendo um pokemon inicial
pokeInicial = int(input(f"Você pode escolher um pokemon inicial para ser seu primeiro parceiro, escolha um\n(1) Bulbasaur\n(2) Squirtle\n(3) Charmander\n"))
if pokeInicial == 1:
     print(f"{pokemonsIniciais[0]}! um tipo planta, otima escolha!\n")
     pokedex.append(pokemonsIniciais[0])
     rep_floresta.append(pokemonsIniciais[0])
if pokeInicial == 2:
     print(f"{pokemonsIniciais[1]}! um tipo água, otima escolha!\n")
     pokedex.append(pokemonsIniciais[1])
if pokeInicial == 3:
     print(f"{pokemonsIniciais[2]}! um tipo fogo, otima escolha!\n")
     pokedex.append(pokemonsIniciais[2])
    
    #escolha do bioma

    
    #checkando validade de escolha
   
escolhas= True
#criando  a escolha do bioma da Floresta
while escolhas == True:
    escolha = int(input(f'\nOque deseja fazer?\n(1) Ir para a Floresta\n(2) Ir para a Caverna\n(3) Pokedex\n() Sair \n>>> '))
    
        
    if escolha == 1 :
        
        pok = random.randint(0, pokemons_mato.index("Abra"))
        
        if pok in rep_floresta:
            print(f'\nVocê encontrou um {pokemons_mato[pok]}, mas você ja possui um!')
            continue
        print(f'\n{pokemons_mato[pok]} apareceu\n')
        
        processo = True
        while processo == True:
            captura = input(f'Você deseja capturar este pokemon? (s/n)')
    
                
            if captura == 's':
                
                    num1=random.randint(0,1)
                    num2=random.randint(0,1)
                    if num1==num2: 
                        print("Você capturou esse pokemon!")
                        pokedex.append(pokemons_mato[pok])
                        rep_floresta.append(pok)
                        break
                    while tentativas > 0:
                        
                        if num1!=num2:
                            novamente=input("você nao conseguiu capturar esse pokemon, deseja tentar novamente? (s/n)")
                            if novamente == 's':
                                tentativas-=1
                                num1=random.randint(0,1)
                                num2=random.randint(0,1)
                                if num1==num2:
                                    print("Você capturou esse pokemon!")
                                    pokedex.append(pokemons_mato[pok])
                                    rep_floresta.append(pok)
                                    break
                                elif num1 != num2:
                                    print("O pokemon fugiu!")
                                    break
                            if novamente == 'n':
                                continue
                    if tentativas == 0:
                        print("\nVocê nao conseguiu capturar este pokemon!")
            if captura == 'n' :
                print(f'\nOk você escolheu não capturar,{pokemons_mato[pok]} ')
                break 
            else:
                print("Escolha uma opção válida!")
            processo = False
            break
                
                        
        
        continue
    
=======
        #escolha randomica de pokemons encontrados na caverna
        pok = random.choice(pokemons_mato)
        print(f"Você entrou na Floresta e encontou um {pok}\n")
    
        #escolha de captura
        captura = input("Você deseja capturar este pokemon? (s/n): \n")
        
        
        #checagem da escolha de captura
        if captura != "s" and captura != "n":
            print('tente novamente com uma opção válida')
        
        #caso o jogador queira tentar capturar
        if captura == 's':
             
                #sorteando a chance de 50% da captura do pokemon
                num1= random.randint(0,1)
                num2= random.randint(0,1)
        
                if num1 == num2: #caso haja captura
                    print(f"Você capturou o {pok}\n")
                    pokedex.append(pok)
                    continue
                while tentativas > 0: #problema aq talvez nao seja while
                
                    if num1 != num2:
                        novamente = input('Voce nao consegui capturar o pokemon!\nDeseja tentar capturar novamente? (s/n) ') #caso não haja captura e o usuarrio recebe novas opções
                        tentativas-=1
                    print(f"Você tem: {tentativas} tentativas")
                    
                    if novamente != 's':
                        print(f'Voce não capturou o {pok}!\n' )
                            
                    if novamente == 's':
                            num1= random.randint(0,3)
                            num2= random.randint(0,3)
                            if num1==num2:
                                print(f"Você capturou o {pok}\n")
                                pokedex.append(pok)
                            elif num1 != num2:
                                print("\nO pokemon fugiu!")
                                break
                        
                            
                    elif novamente == 'n':
                            print(f"Ok, você escolheu não capturar o {pok}.\n")  
        
                    elif captura == 'n':
                        print(f"Ok, você escolheu não capturar o {pok}.")  
            
>>>>>>> f16240e657f5f1f69ef6941712a7b146cb36767e
    #caso a escolha seja a da carverna
    if escolha == 2:
        
        #escolha randomica de pokemons encontrados na caverna
        pok = random.choice(pokemons_caverna)
        print(f"Você entrou na caverna e encontou um {pok}\n")
    
        #escolha de captura
        captura = input("Você deseja capturar este pokemon? (s/n): \n")
        
        
        #checagem da escolha de captura
        if captura != "s" and captura != "n":
            print('tente novamente com uma opção válida')
        
        #caso o jogador queira tentar capturar
        if captura == 's':
            
                #sorteando a chance de 30% da captura do pokemon
                num1= random.randint(0,3)
                num2= random.randint(0,3)
        
                if num1 == num2: #caso haja captura
                    print(f"Você capturou o {pok}\n")
                    pokedex.append(pok)
                    continue
                while tentativas > 0: #problema aq talvez nao seja while
                
                    if num1 != num2:
                        novamente = input('Voce nao consegui capturar o pokemon!\nDeseja tentar capturar novamente? (s/n) ') #caso não haja captura e o usuarrio recebe novas opções
                        tentativas-=1
                    print(f"Você tem: {tentativas} tentativas")
                    
                    if novamente != 's':
                        print(f'Voce não capturou o {pok}!\n' )
                            
                    if novamente == 's':
                            num1= random.randint(0,3)
                            num2= random.randint(0,3)
                            if num1==num2:
                                print(f"Você capturou o {pok}\n")
                                pokedex.append(pok)
                            elif num1 != num2:
                                print("\nO pokemon fugiu!")
                                break
                        
                            
                    elif novamente == 'n':
                            print(f"Ok, você escolheu não capturar o {pok}.\n")  
        
                    elif captura == 'n':
                        print(f"Ok, você escolheu não capturar o {pok}.")
        
    if escolha == 3:
        if len(pokedex) <1 :
            print("Você ainda não capturou nenhum pokemon! ")
        print(f"Aqui são todos os pokemons que você ja capturou {pokedex}") 
    
    if tentativas == 0: #nao esta funcionando 
            print("Você atingiu o limite de tentativas extras!")
            continue
    
    if escolha == 4:
        print("Até logo!")
<<<<<<< HEAD
        break
=======
        break
>>>>>>> f16240e657f5f1f69ef6941712a7b146cb36767e
