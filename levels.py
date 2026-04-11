
import os
import combat
import inimigos
import charactere
import musicas

class Levels:


    def __init__(self,player):

        self.player=player

    def selector_level(self,level):
        self.level=level
        if self.level==1:
            self.level_1()
        elif self.level==2:
            self.level_2()
    def level_1(self,enemy=inimigos.enemy):
        self.enemy=enemy
        self.enemy_talk=[f'ora ora se não é o {self.player.name}',f'é o que veremos!']
        self.charactere_talk=[f'você não irá me impedir monstro asqueroso']
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'MONSTRO- {self.enemy_talk[0]}\n\n\n')
        input('     O                                                  [ENTER-->] ')
        musicas.som_clik.play()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{self.player.name}- {self.charactere_talk[0]}\n\n\n')
        input('                           O                            [ENTER-->] ')
        musicas.som_clik.play()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'MONSTRO- É O QUE VEREMOS!\n\n\n')
        input('                                                   O    [ENTER-->] ')
        musicas.som_clik.play()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('====================VOCÊ INICIOU UM COMBATE!====================')
        fase_1=combat.Combat(self.player,self.enemy)
        while self.enemy.life>0 and self.player.life>0:
            fase_1.atack_player()
            os.system('cls' if os.name == 'nt' else 'clear')
            fase_1.atack_enemy()
            os.system('cls' if os.name == 'nt' else 'clear')
        if self.player.life==0:
            musicas.parar_musica()
            musicas.musica_morreu()
            print('life')
            print('🕸️')
            print('\n\n\n\n\n')
            print('👻  🦤')
            print('\n\n\n\n\n')
            print('VOCÊ MORREU , BRUTAL')
            self.player.level=1
            self.player.life=3
            self.enemy.life=3
            input('                                                        [ENTER-->] ')
            musicas.som_clik.play()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            musicas.parar_musica()
            musicas.som_vitoria.play()
            print('VOCÊ DERROTOU O MONSTRO')
            self.player.coins+=self.enemy.coins
            print(f'você recebeu {self.enemy.coins} de ouro por esse abate!')
            input('                                                   O    [ENTER-->] ')
            musicas.som_clik.play()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player.level=2

    def level_2(self,enemy2=inimigos.enemy2):
        self.enemy2=enemy2
        self.talks=[f'{inimigos.enemy2.name}-Você conseguiu derrotar meu irmão \
mais novo e burro, mas nunca conseguirá \
me vencer {self.player.name}',f'{self.player.name}-kkkkk',
f'{inimigos.enemy2.name}- Do que você está rindo?',f'{self.player.name}-Estou rindo dessa sua \
cara de SHIBATA! que eu vou ter que pisar com minha \
bota suja de merda!',f'{inimigos.enemy2.name}-ORA SEU FILHO DA PUTA INSOLENTE!!!']
        for talk in self.talks:
            print(talk)
            input('                                                        [ENTER-->] ')
            musicas.som_clik.play()
            os.system('cls' if os.name == 'nt' else 'clear')

        print('====================VOCÊ INICIOU UM COMBATE!====================')
        fase_2=combat.Combat(self.player,self.enemy2)
        while self.enemy2.life>0 and self.player.life>0:
            fase_2.atack_player()
            os.system('cls' if os.name == 'nt' else 'clear')
            fase_2.atack_enemy()
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.player.life<=0:
                musicas.parar_musica()
                musicas.musica_morreu()
                print('life')
                print('🕸️')
                print('\n\n\n\n\n')
                print('👻  🦤')
                print('\n\n\n\n\n')
                print('VOCÊ MORREU , BRUTAL')
                self.player.level=2
                self.player.life=3
                self.enemy2.life=10
                input('                                                        [ENTER-->] ')
                musicas.som_clik.play()
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            if self.enemy2.life <=0:
                musicas.parar_musica()
                musicas.som_vitoria.play()
                print('VOCÊ DERROTOU O MONSTRO')
                self.player.coins+=self.enemy2.coins
                print(f'você recebeu {self.enemy2.coins} de ouro por esse abate!')
                input('                                                   O    [ENTER-->] ')
                musicas.som_clik.play()
                os.system('cls' if os.name == 'nt' else 'clear')
                

if __name__=='__main__':
    player_teste=charactere.Charactere()
    teste=Levels(player_teste)
    teste.level_1()
    teste.level_2()

