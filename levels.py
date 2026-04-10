
import os
import combat

class Levels:


    def __init__(self,player,enemy):

        self.player=player
        self.enemy=enemy

    def selector_level(self,number_level):
        if number_level==1:
            self.level_1()
    def level_1(self):
        self.enemy_talk=[f'ora ora se não é o {self.player.name}',f'é o que veremos!']
        self.charactere_talk=[f'você não irá me impedir monstro asqueroso']
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'MONSTRO- {self.enemy_talk[0]}\n\n\n')
        input('     O                                                  [ENTER-->] ')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{self.player.name}- {self.charactere_talk[0]}\n\n\n')
        input('                           O                            [ENTER-->] ')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'MONSTRO- É O QUE VEREMOS!\n\n\n')
        input('                                                   O    [ENTER-->] ')
        os.system('cls' if os.name == 'nt' else 'clear')
        print('====================VOCÊ INICIOU UM COMBATE!====================')
        fase_1=combat.Combat(self.player,self.enemy)
        while self.enemy.life>0 and self.player.life>0:
            fase_1.atack_player()
            os.system('cls' if os.name == 'nt' else 'clear')
            fase_1.atack_enemy()
            os.system('cls' if os.name == 'nt' else 'clear')
        if self.player.life==0:
            print('VOCÊ MORREU , BRUTAL')
        else:
            print('VOCÊ DERROTOU O MONSTRO')
            self.player.coins+=self.enemy.coins
            print(f'você recebeu {self.enemy.coins} de ouro por esse abate!')

        