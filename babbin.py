import random
pokeFloresta = ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie', 'Weedle', 'Pidgey', 'Rattata', 'Spearow', 'Ekans', 'Pikachu', 'Nidoran(M)', 'Nidoran(F)', 'Vulpix', 'Clefairy', 'Jigglypuff', 'Oddish', 'Paras', 'Venonat', 'Meowth', 'Psyduck', 'Mankey', 'Growlithe', 'Poliwag', 'Bellsprout', 'Tentacool', 'Ponyta', 'Slowpoke', 'Farfetchd', 'Doduo', 'Seel', 'Shellder', 'Krabby', 'Exeggcute', 'Lickitung', 'Chansey', 'Horsea', 'Goldeen', 'Staryu', 'Scyther', 'Tauros', 'Magikarp', 'Lapras', 'Eevee', 'Omanyte', 'Aerodactyl', 'Articuno', 'Zapdos', 'Moltres']
pokeCaverna = ['Sandshrew', 'Zubat', 'Diglett', 'Abra', 'Machop', 'Geodude', 'Magnemite', 'Grimer', 'Gastly', 'Onix', 'Drowzee', 'Hypno', 'Voltorb', 'Cubone', 'Hitmonlee', 'Hitmonchan', 'Koffing', 'Rhyhorn', 'Tangela', 'Kangaskhan', 'Mr. Mime', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Ditto', 'Porygon', 'Kabuto', 'Snorlax', 'Dratini', 'Mewtwo', 'Mew']
pokedex = []
repetidosFloresta = []
repetidosCaverna = []
pokebolas = int(0)
soma = int(0)
introducao = True
while introducao == True:
    nomeacao = True
    while nomeacao == True:
        nome = input(f'\n??? - Olá viajante, qual o seu nome?\n-> ')
        if nome.isdigit() == True:
            print('\nUse um nome com letras')
            continue
        certo = input(f'\nO nome {nome} está correto? (Sim/Não): ')
        if certo == 'Não' and certo.isdigit() == False:
            continue
        if certo == 'Sim' and certo.isdigit() == False:
            nomeacao = False
        else:
            print(f'\nEscolha uma opção válida')
            continue
    print(f'\nProfessor Carvalho - Bem vindo {nome}, eu sou o Professor Carvalho, e estou aqui para te auxiliar nessa sua incrível jornada Pokémon!\n')
    conversa = True
    while conversa == True:
        fala = input(f'[1] Pokémon? o que é isso?\n[2] Onde é que eu estou?\n-> ')
        if fala == '1':
            print(f'\n{nome} - Pokémon? o que é isso?')
            print(f'Professor Carvalho - O que é um Pokémon?\nProfessor Carvalho - Os Pokémons são criaturas incríveis que compartilham o mundo com os seres humanos\nProfessor Carvalho - Atualmente, existem centenas de espécies de Pokémon documentadas\nProfessor Carvalho - A sua incrível tarefa é capturar, treinar e lutar com todos eles\n')
            conversa = False
        if fala == '2':
            print(f'\n{nome} - Onde é que eu estou?')
            print(f'Professor Carvalho - Você está em Unova, e a sua incrível tarefa é capturar, treinar e lutar com todos os Pokémons\n')
            conversa = False
        if fala != '1' and fala != '2':
            print('\nEscolha das opções\n')
            continue
    conversa = True
    while conversa == True:
        fala = input('[1] Como posso capturar um Pokémon?\n[2] Tudo bem, isso parece simples!\n-> ')
        if fala == '1':
            print(f'\n{nome} - Como posso capturar um Pokémon?')
            print(f'Professor Carvalho - Isso é simples, basta usar uma pokebola!\nProfessor Carvalho - Quando você arremessa e acerta um Pokémon com uma pokebola, existe uma chance de captura que varia para cada Pokemon!\nProfessor Carvalho - Aqui estão algumas, para que você possa pegar alguns Pokemons!\n')
            conversa = False
        if fala == '2':
            print(f'\n{nome} - Tudo bem, isso parece simples!')
            print('Professor Carvalho - Gostei dessa confiança!\nProfessor Carvalho - Aqui estão algumas pokebolas, para que você possa pegar alguns Pokémons!\n')
            conversa = False
        if fala != '1' and fala != '2':
            print('\nEscolha das opções\n')
            continue
    print('*Você recebeu 10 pokebolas*\n')
    print('Professor Carvalho - Agora vá caçar alguns Pokémons!')
    pokebolas += 10
    jornada = True
    introducao = False
while jornada == True:
    jogo = input(f'\nOque deseja fazer?\n[1] Ir para a Floresta\n[2] Ir para a Caverna\n[3] Explorar\n[4] Pokedex\n[5] Sair (O jogo não será salvo)\n-> ')
    if jogo == '1' and pokebolas > 0:
        pokeAleatorio = random.randint(0, pokeFloresta.index('Moltres'))
        if pokeAleatorio in repetidosFloresta:
            print(f'\nVocê encontrou um {pokeFloresta[pokeAleatorio]}, mas você ja possui um!')
            continue
        print(f'\n{pokeFloresta[pokeAleatorio]} apareceu\n')
        processo = True
        while processo == True:
            captura = input(f'Você deseja captura-lo? Você tem 3 chances (Sim/Não)\n-> ')
            if captura == 'Sim':
                for i in range(1, 4):
                    sorte = random.randint(1, 100)
                    pokebolas -= 1
                    if sorte < 51 and i > 0 and pokebolas > 0:
                        pokedex.append(pokeFloresta[pokeAleatorio])
                        print(f'\nVocê capturou {pokeFloresta[pokeAleatorio]}\n')
                        print(f'*Você ainda tem {pokebolas} pokebolas*')
                        repetidosFloresta.append(pokeAleatorio)
                        soma += 1
                        processo = False
                        break
                    elif sorte > 50 and i == 1 and pokebolas > 0:
                        continuar = input(f'\nVocê não conseguiu pegar {pokeFloresta[pokeAleatorio]}, quer tentar denovo? Você tem mais 2 tentativas (Sim/Não)\n-> ')
                        if continuar == 'Não':
                            break
                    elif sorte > 50 and i == 2 and pokebolas > 0:
                        continuar = input(f'\nVocê não conseguiu pegar {pokeFloresta[pokeAleatorio]}, quer tentar denovo? Você tem mais 1 tentativa (Sim/Não)\n-> ')
                        if continuar == 'Não':
                            break
                    elif sorte > 50 and i == 3:
                        print(f'\n{pokeFloresta[pokeAleatorio]} fugiu\n')
                        print(f'*Você ainda tem {pokebolas} pokebolas*')
                        processo = False
                        break
                    else:
                        print(f'\n{pokeFloresta[pokeAleatorio]} fugiu e acabaram suas pokebolas')
                        pokebolas = 0
                        processo = False
                        break
            if captura == 'Não':
                processo = False
            if captura != 'Não' and captura != 'Sim':
                print('\nEscolha uma opção válida')
                continue
        continue
    
    elif jogo == '2' and pokebolas > 0:
        pokeAleatorio = random.randint(0, pokeCaverna.index('Mew'))
        if pokeAleatorio in repetidosCaverna:
            print(f'\nVocê encontrou um {pokeCaverna[pokeAleatorio]}, mas você ja possui um!')
            continue
        print(f'\n{pokeCaverna[pokeAleatorio]} apareceu\n')
        processo = True
        while processo == True:
            captura = input(f'Você deseja captura-lo? Você tem 3 chances (Sim/Não)\n-> ')
            if captura == 'Sim':
                for i in range(1, 4):
                    sorte = random.randint(1, 100)
                    pokebolas -= 1
                    if sorte < 36 and i > 0 and pokebolas > 0:
                        pokedex.append(pokeCaverna[pokeAleatorio])
                        print(f'\nVocê capturou {pokeCaverna[pokeAleatorio]}\n')
                        print(f'*Você ainda tem {pokebolas} pokebolas*')
                        repetidosCaverna.append(pokeAleatorio)
                        soma =+ 1
                        processo = False
                        break
                    elif sorte > 35 and i == 1 and pokebolas > 0:
                        continuar = input(f'\nVocê não conseguiu pegar {pokeCaverna[pokeAleatorio]}, quer tentar denovo? Você tem mais 2 tentativas (Sim/Não)\n-> ')
                        if continuar == 'Não':
                            break
                    elif sorte > 35 and i == 2 and pokebolas > 0:
                        continuar = input(f'\nVocê não conseguiu pegar {pokeCaverna[pokeAleatorio]}, quer tentar denovo? Você tem mais 1 tentativa (Sim/Não)\n-> ')
                        if continuar == 'Não':
                            break
                    elif sorte > 35 and i == 3:
                        print(f'\n{pokeCaverna[pokeAleatorio]} fugiu\n')
                        print(f'Você ainda tem {pokebolas} pokebolas')
                        processo = False
                        break
                    else:
                        print(f'\n{pokeCaverna[pokeAleatorio]} fugiu e acabaram suas pokebolas')
                        pokebolas = 0
                        processo = False
                        break
            if captura == 'Não':
                processo = False
            if captura != 'Não' and captura != 'Sim':
                print('\nEscolha uma opção válida')
                continue
        continue
    if jogo == '3':
        explorar = random.randint(1, 5)
        pokebolas += explorar
        print(f'\nVocê explorou e achou {explorar} pokebolas!\n*Você agora tem {pokebolas} pokebolas*')
        continue
    if jogo == '4':
        if len(pokedex) < 1:
            print('\nVocê ainda não tem nenhum Pokémon!')
        else:
            print(f'\nEsses são seus Pokémons: {pokedex}')
    if jogo != '1' and jogo != '2' and jogo != '3' and jogo != '4' and jogo != '5':
        print(f'\nEscolha uma opção válida')
        continue
    if jogo == '5':
        print(f'\nEsses foram todos os Pokémons que você pegou: {pokedex}\nAo todo foram {soma} Pokémons\nObrigado por jogar\n')
        jornada = False
    if pokebolas <= 0:
        print(f'\nVocê está com {pokebolas} pokebolas vá explorar')
        continue