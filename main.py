from levels import Levels
from charactere import Charactere
from items import Items
import os
import musicas

init_game=True

level=1
player=Charactere(level=1)
player.creat_caractere()
player.coins=10

while init_game:


    musicas.musica_normal()
    
    response=int(input(f'Deseja prosseguir para o level {player.level} ou fazer outra coisa?\n\
[1]para prosseguir\n\
[2]para abrir a loja\n\
[3]para exibir os status'))
    os.system('cls' if os.name == 'nt' else 'clear')
    if response==1:
        musicas.parar_musica()
        musicas.musica_batalha()
        Levels(player).selector_level(player.level)
        musicas.parar_musica()
        musicas.musica_normal()
    elif response==2:
        Items().buy(player)
    elif response==3:
        print(player.status())
    else:
        print('saindo...')
        init_game=False