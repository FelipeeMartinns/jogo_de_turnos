


class Charactere:

    def __init__(self,name=None,life=10,coins=None,skills=None,armor_ad=None,armor_ap=None,damage_ad=1,damage_ap=None):
        self.name=name
        self.life=life
        self.charactere_coins=coins
        self.skills=skills
        self.armor_ad=armor_ad
        self.armor_ap=armor_ap
        self.damage_ad=damage_ad
        self.damage_ap=damage_ap

    def creat_caractere(self):

        self.name=input('Digite seu nome:\n')

    def mostrar_dinheiro(self):
        return self.charactere_coins