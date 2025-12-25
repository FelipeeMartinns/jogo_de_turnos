


class Charactere:

    def __init__(self, name="player", life=100, coins=0):
        self.name = name
        self.life = life
        self.max_life = life
        self.coins = coins

        # atributos de combate
        self.damage_ad = 5
        self.damage_ap = 0
        self.armor_ad = 0
        self.armor_ap = 0

        # habilidades
        self.skills = []

    def creat_caractere(self):
        while True:
            self.name = input('Digite seu nome:\n')
            confirm = input(
                f'Você confirma o nome {self.name}? [S]im ou [N]ão: '
            ).upper()

            if confirm.startswith('S'):
                break

    def status(self):
        return (
            f'{self.name}\n'
            f'ATAQUE FÍSICO: {self.damage_ad}\n'
            f'ATAQUE MÁGICO: {self.damage_ap}\n'
            f'DEFESA: {self.armor_ad} AD | {self.armor_ap} AP\n'
            f'SKILLS: {self.skills}'
        )
