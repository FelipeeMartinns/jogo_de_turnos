


class Levels:


    def __init__(self,charactere,enemy):

        self.charactere=charactere
        self.enemy=enemy

    def level_1(self):
        self.enemy_talk=[f'ora ora se não é o {self.charactere.name}',f'é o que veremos!']
        self.charactere_talk=[f'você não irá me impedir monstro asqueroso']