while True:
    import random

    pokemons_caverna=['Aggron','Larvitar','Aron','Pupitar']
    pokemons_mato=['bulbasaur','Pansage','Turtwig','Treecko']
    pokedex=[]
#escolha do bioma
    
    escolha=int(input("Escolha para onde deseja ir\n1. Ir para o Mato\n2. Ir para a Caverna\n3. Abrir Pokedex\n4. Sair\n:"))
    if escolha >4:
        print("\nNão foi possível encontrar alguma função com este número digitado!\n")
        continue
    if escolha == 1:
        
        pok=random.choice(pokemons_mato)
        print(f"Você entrou no mato e encontou um {pok}\n")
        captura=input("Você deseja capturar este pokemon? (s/n): \n")
        if captura == 's':
            print(f"Você capturou o {pok}\n")
               
        elif captura == 'n':
            print(f"Ok, você escolheu não capturar o {pok}")  
    if escolha == 3:
        print(pokedex)
            
      
        
   