class Items:

    def __init__(self):
        # espada
        self.sword_price = 10
        self.sword_damage_ad = 5

        # cajado
        self.staff_price = 10
        self.staff_damage_ap = 5

        # armadura
        self.armor_price = 5
        self.armor_ad = 2
        self.armor_ap = 2

    def buy_sword(self, player):
        if player.coins >= self.sword_price:
            player.coins -= self.sword_price
            player.damage_ad += self.sword_damage_ad
            return True
        return False

    def buy_staff(self, player):
        if player.coins >= self.staff_price:
            player.coins -= self.staff_price
            player.damage_ap += self.staff_damage_ap
            return True
        return False

    def buy_armor(self, player):
        if player.coins >= self.armor_price:
            player.coins -= self.armor_price
            player.armor_ad += self.armor_ad
            player.armor_ap += self.armor_ap
            return True
        return False
