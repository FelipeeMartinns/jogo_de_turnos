class Combat:

    def attack(self, attacker, defender):
        damage = attacker.damage_ad - defender.armor_ad

        if damage < 1:
            damage = 1

        defender.life -= damage
        return damage

    def is_dead(self, entity):
        return entity.life <= 0
