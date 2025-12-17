


class Charactere:

    def __init__(self,name=None,life=10,coins=None,skills=None,armor_ad=None,armor_ap=None,damage_ad=1,damage_ap=None):
        self.name=name
        self.life=life
        self.coins=coins
        self.skills=skills
        self.armor_ad=armor_ad
        self.armor_ap=armor_ap
        self.damage_ad=damage_ad
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