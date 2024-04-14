import random

pokemons_caverna=['Aggron','Larvitar','Aron','Pupitar']
pokemons_mato=['bulbasaur','Pansage','Turtwig','Treecko']
pokedex=[]
tentativas = 3
    
print(f"professor carvalho aparece")

nomeJogador = input(f"Professor Carvalho - olá treinador, bem vindo ao mundo Pokemón. Eu sou o professor Carvalho, como posso te chamar? \nDigite aqui seu nome: ")

print(f"Professor carvalho - É um prazer te conhecer, {nomeJogador}. Esta é a cidade de Pallet, da região de Kanto!\n")
    
#escolha do bioma
for i in range(0,10):  
   
    escolha=int(input("Escolha para onde deseja ir\n1. Ir para o Mato\n2. Ir para a Caverna\n3. Abrir Pokedex\n4. Sair\n:"))
    
    if escolha >4 or escolha<0:
        print("\nNão foi possível encontrar alguma função com este número digitado!\n")
    

    if escolha == 1:
        
        pok=random.choice(pokemons_mato)
        print(f"Você entrou no mato e encontou um {pok}\n")
        captura=input("Você deseja capturar este pokemon? (s/n): \n")
        
        if captura == 's':
            num1= random.randint(0,1)
            num2= random.randint(0,1)
           
            if num1 == num2:
                print(f"Você capturou o {pok}\n")
                pokedex.append(i)
            else:
                nova=input('Voce nao consegui capturar o pokemon!\nDeseja tentar capturar novamente? (s/n) ')
               
                if nova != 's':
                    print(f'Voce capturou o {pok}!\n' )
                    tentativas-=1
                  
                    if nova == 's':
                        print(f"Você capturou o {pok}\n")
                    
                    elif nova == 'n':
                        print(f"Ok, você escolheu não capturar o {pok}.\n")  
               
                elif captura == 'n':
                    print(f"Ok, você escolheu não capturar o {pok}.\n")  
   
    if escolha == 3:
        print(pokedex)
    if escolha == 4:
        print("Até logo!")
        break
