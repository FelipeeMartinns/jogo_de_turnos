from charactere import Charactere
from enemy import Enemy

class Combat:

    def __init__(self,player,enemy):
        
        self.player=player
        self.enemy=enemy
        self.life=''

    def life_bar(self):
        
        for qnt_life in range(self.player.life):
            self.life+=f'-'
        for qnt_life in self.life:
            print(f'{qnt_life}',end=' ')

fase_1=Combat(Charactere('felipe'),Enemy('slime'))

fase_1.life_bar()