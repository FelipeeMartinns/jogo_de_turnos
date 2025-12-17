
import os


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
        os.system('cls')
        print(f'MONSTRO- {self.enemy_talk[0]}\n\n\n')
        input('     O                                                  [ENTER-->] ')
        os.system('cls')
        print(f'{self.player.name}- {self.charactere_talk[0]}\n\n\n')
        input('                           O                            [ENTER-->] ')
        os.system('cls')
        print(f'MONSTRO- É O QUE VEREMOS!\n\n\n')
        input('                                                   O    [ENTER-->] ')
        os.system('cls')
        print('====================VOCÊ INICIOU UM COMBATE!====================')

        