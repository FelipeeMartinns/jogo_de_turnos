from levels import Levels
from charactere import Charactere
from enemy import Enemy
from items import Items


init_game=True

level=1
player=Charactere()
player.creat_caractere()
enemy=Enemy('monstro',10,1,damage_ad=1,weakness='fogo')
while init_game:
    
    response=int(input(f'Deseja prosseguir para o level {level} ou ir a loja? [1]para prosseguir e [2]para abrir a loja'))
    if response==1:
        Levels(player,enemy)
    elif response==2:
        Items().buy(player)
    else:
        print('saindo...')
        init_game=False