

class Enemy:

    def __init__(self, name="slime", life=50, damage_ad=3, coins=5):
        self.name = name
        self.life = life
        self.max_life = life

        # combate
        self.damage_ad = damage_ad
        self.damage_ap = 0
        self.armor_ad = 0
        self.armor_ap = 0

        # recompensa
        self.coins = coins

        # características
        self.weakness = None
