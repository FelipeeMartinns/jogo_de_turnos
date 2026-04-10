from charactere import Charactere
from enemy import Enemy
import random
import os

class Combat:

    def __init__(self,player,enemy,turno=0):
        
        self.player=player
        self.enemy=enemy
        self.life=''
        self.turno=turno

    def life_bar(self):
        self.life=''
        for qnt_life in range(self.player.life):
            self.life+=f'❤️'
        for qnt_life in self.life:
            print(f'{qnt_life}',end=' ')

    def atack_player(self):

        print('life')
        self.life_bar()
        print('\n\n\n\n\n')
        print('🙉  🦤')
        print('\n\n\n\n\n')
        acao=int(input('[1]ATACAR  [2]DEFENDER [3]PULAR TURNO'))
        os.system('cls' if os.name == 'nt' else 'clear')
        if acao==1:
            print('life')
            self.life_bar()
            print('\n\n\n\n\n')
            print('  🙉💥🦤')
            print('\n\n\n\n\n')
            print('vc atacou o monstro!')
            self.enemy.life-=self.player.damage_ad
            self.player.defesa=False
        elif acao==2:
            print('life')
            self.life_bar()
            print('\n\n\n\n\n')
            print('🙊  🦤')
            print('\n\n\n\n\n')
            print('você está em posição de defesa')
            self.player.defesa=True

        else:
            print('life')
            self.life_bar()
            print('\n\n\n\n\n     ?')
            print('🙈  🦤')
            print('\n\n\n\n\n')
            print('vc pulou o turno!')
        input('                                                        [ENTER-->] ')

    def atack_enemy(self):
        print('life')
        self.life_bar()
        print('\n\n\n\n\n')
        print('🙉  🦤')
        print('\n\n\n\n\n')
        if random.randint(0,1) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.player.defesa==True:
                print('life')
                self.life_bar()
                print('\n\n\n\n\n')
                print('🙊💫🦤  ')
                print('\n\n\n\n\n')
                print('Monstro tentou acertar um golpe em você mas você defendeu!')
            else:
                print('life')
                self.life_bar()
                print('\n\n\n\n\n')
                print('🙉💥🦤  ')
                print('\n\n\n\n\n')
                print('Monstro acertou um golpe em você!')
                self.player.life-=self.enemy.damage_ad
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('life')
            self.life_bar()
            print('\n\n\n\n\n')
            print('🦤  🙉 ')
            print('\n\n\n\n\n')
            
            print('Monstro tentou acertar um golpe em você e errou!')
        input('                                                        [ENTER-->] ')

        

