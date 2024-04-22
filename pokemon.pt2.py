#importando biblioteca randomica
import random

#criando listas e variaveis
pokemonsIniciais = ["Bulbasaur","Squirtle","Charmander"]
pokemons_caverna = ['Onix','Zubat','Diglet','Geodude','Grimer','Gastly','Hypno','Voltorb','Cubone']
pokemons_mato = ['Pidgey','Caterpie','Bellsprout','Abra','Weedle','Ekans','Pikachu','Spearow']
rep_floresta = []
rep_caverna = []
pokedex = []
tentativas = 3
    
#introdução professor carvalho, e escolha de um nome para o jogador
print(f"Professor Carvalho aparece")
nomeJogador = input(f"Professor Carvalho - Olá treinador, bem vindo ao mundo Pokemón. Eu sou o professor Carvalho, como posso te chamar? \nDigite aqui seu nome: ")
print(f"\nProfessor carvalho - É um prazer te conhecer, {nomeJogador}. Esta é a cidade de Pallet, da região de Kanto!\n")


    
#escolha do bioma   
escolhas= True
#criando  a escolha do bioma da Floresta
while escolhas == True:
    escolha = int(input(f'\nO que deseja fazer?\n(1) Ir para a Floresta\n(2) Ir para a Caverna\n(3) Pokedex\n(4) Sair \n>>> '))
    if escolha == 1 :
        
        pok = random.randint(0, pokemons_mato.index("Spearow"))
        
        if pok in rep_floresta:
            print(f'\nVocê encontrou um {pokemons_mato[pok]}, mas você ja possui este pokémon!')
            continue
        print(f'\n*{pokemons_mato[pok]} apareceu*\n')
        
        capt = True
        while capt == True:
            captura = input(f'Você deseja capturar este pokémon? (s/n)\n>>>')
    
            
            if captura == 's':
                
                    num1 = random.randint(0,1)
                    num2 = random.randint(0,1)
                    if num1 == num2: 
                        print("Você capturou esse pokémon!")
                        pokedex.append(pokemons_mato[pok])
                        rep_floresta.append(pok)
                        break
                    while tentativas > 0:
                        
                        if num1 != num2:
                            novamente = input("você nao conseguiu capturar esse pokemon, deseja tentar novamente? (s/n)\n>>>")
                        
                            if novamente == 's':
                                tentativas -= 1
                                num1 = random.randint(0,1)
                                num2 = random.randint(0,1)
                                if num1 == num2:
                                    print("Você capturou esse pokémon!")
                                    pokedex.append(pokemons_mato[pok])
                                    rep_floresta.append(pok)
                                    break
                                elif num1 != num2:
                                    print("O pokémon fugiu!")
                                    break
                            if novamente == 'n':
                                 continue
                            elif novamente != 's' and novamente != 'n':  
                                print("Tente com uma opção válida!")
                               
                    if tentativas == 0:
                        
                        print("\nVocê não conseguiu capturar este pokemon!")
                        print("Você atingiu o limite de tentativas!")
            elif captura != 's' and captura!= 'n':  
                print("Escolha uma opção válida!")
            
                                   
            if captura == 'n' :
                print(f'\nOk você escolheu não capturar,{pokemons_mato[pok]} ')
                
                break 

                    
            capt = False
            break
                
                        
        
        continue
    
    #caso a escolha seja a da carverna
    if escolha == 2 :
        
        pok = random.randint(0, pokemons_caverna.index("Cubone"))
        
        if pok in rep_caverna:
            print(f'\nVocê encontrou um {pokemons_caverna[pok]}, mas você já possui este pokémon!')
            continue
        print(f'\n{pokemons_caverna[pok]} apareceu\n')
        
        capt = True
        while capt == True:
            captura = input(f'Você deseja capturar este pokémon? (s/n)\n>>>')
    
                
            if captura == 's':
                
                    num1 = random.randint(0,1)
                    num2 = random.randint(0,1)
                    if num1 == num2: 
                        print("Você capturou esse pokémon!")
                        pokedex.append(pokemons_caverna[pok])
                        rep_caverna.append(pok)
                        break
                    while tentativas > 0:
                        
                        if num1 != num2:
                            novamente = input("você nao conseguiu capturar esse pokémon, deseja tentar novamente? (s/n)\n>>> ")
                            if novamente == 's':
                                tentativas -= 1
                                num1 = random.randint(0,1)
                                num2 = random.randint(0,1)
                                if num1 == num2:
                                    print("Você capturou esse pokémon!")
                                    pokedex.append(pokemons_caverna[pok])
                                    rep_caverna.append(pok)
                                    break
                                elif num1 != num2:
                                    print("O pokémon fugiu!")
                                    break
                            if novamente == 'n':
                                continue
                            elif novamente != 's' and novamente != 'n':
                                print(f"\n*Digite uma opção válida!*")
                    if tentativas == 0:
                        print("\nVocê não conseguiu capturar este pokémon!")
                        print("Você atingiu o limite de tentativas!")
            if captura == 'n' :
                print(f'\nOk você escolheu não capturar,{pokemons_caverna[pok]} ')
                break 
            elif captura != 's' and captura != 'n':
                print("\n*Escolha uma opção válida!*")
            capt = False
            break
        
    if escolha == 3:
        if len(pokedex) < 1 :
            print("Você ainda não capturou nenhum pokémon! ")
        print(f"Aqui são todos os pokémon que você ja capturou {pokedex}") 
    
    if escolha == 4:
        print("Até logo!")
        break
