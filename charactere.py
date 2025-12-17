


class Charactere:

    def __init__(self,name=None,life=10,coins=None,skills=None,armor_ad=None,armor_ap=None,damage_ad=1,damage_ap=None):
        if name is None:
            self.name='player'
        else:
            self.name=name
        self.life=life
        if coins is None:
            self.coins=0
        else:
            self.coins=coins 
        if skills is None:
            self.skills=[]
        else:
            self.skills=skills
        if armor_ad is None:
            self.armor_ad=0
        else:
            self.armor_ad=armor_ad
        if armor_ap is None:
            self.armor_ap=0
        else:
            self.armor_ap=armor_ap
        if damage_ad is None:
            self.damage_ad=0
        else:
            self.damage_ad=damage_ad
        if damage_ap is None:
            self.damage_ap=0
        else:
            self.damage_ap=damage_ap

    def creat_caractere(self):

        while True:
            self.name=input('Digite seu nome:\n')
            confirm= input(f'você confimar o nome {self.name} ? [S]im ou [N]ão').upper()
            if confirm.startswith('S') == True:
                break
    def status(self):

        return f'{self.name}\n\
ATAQUE FÍSICO: {self.damage_ad}\n\
ATAQUE MÁGICO: {self.damage_ap}\n\
DEFESA: {self.armor_ad} AD | {self.armor_ap} AP\n\
SKILLS: {self.skills}'