from levels import Levels
from charactere import Charactere
from enemy import Enemy
from items import Items


init_game=True

level=1
player=Charactere()
player.creat_caractere()
player.coins=10
enemy=Enemy('monstro',10,1,damage_ad=1,weakness='fogo')
while init_game:
    
    response=int(input(f'Deseja prosseguir para o level {level} ou ir a loja? [1]para prosseguir e [2]para abrir a loja ou [3] para exibir os status'))
    if response==1:
        Levels(player,enemy).selector_level(level)
    elif response==2:
        Items().buy(player)
    elif response==3:
        print(player.status())
    else:
        print('saindo...')
        init_game=False