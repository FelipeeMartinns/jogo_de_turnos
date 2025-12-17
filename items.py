from charactere import Charactere

class Items:

    def __init__(self):
        self.sword()
        self.staff()
        self.armor_basic()
    
    def sword(self):
        self.name_sword='espada'
        self.value_item_sword= 10
        self.damage_ad_sword=5
        self.description_sword='uma espadada normal que aumenta seu dano fisico em 5'

    def staff(self):
        self.name_staff='cajado'
        self.value_item_staff=10
        self.damage_ap=5
        self.description_staff='um cajado comum que aumenta seu dano magico em 5'

    def armor_basic(self):
        self.name_armor_basic='armadura'
        self.value_item_armor_basic=5
        self.armor_ad=2
        self.armor_ap=2
        self.description_armor_basic='uma armadura normal que aumenta sua resistencia fisica e mágica em 2'

    def buy(self,player):

        print(f'=========LOJA DO ISAAC=========\n\
ATAQUE FÍSICO:\n\
{self.name_sword} -- {self.description_sword}\n\
{self.value_item_sword} COINS\n[BUY->[1]<-]\n\n\
ATAQUE MÁGICO:\n\
{self.name_staff} -- {self.description_staff}\n\
{self.value_item_staff} COINS\n[BUY->[2]<-]\n\n\
DEFESA:\n\
{self.name_armor_basic} -- {self.description_armor_basic}\n\
{self.value_item_armor_basic} COINS\n[BUY->[3]<-]\n\n\n\
                                                                        COINS= {player.coins}')
        try:
            response=int(input(''))

            if response==1 and player.coins>= self.value_item_sword:
                player.damage_ad+=self.damage_ad_sword
                player.coins-=self.value_item_sword
                print('AD + 5')
            elif response==2 and player.coins>= self.value_item_staff:
                player.damage_ad+=self.damage_ap
                player.coins-=self.value_item_staff
                print('AP + 5')
            elif response==3 and player.coins>= self.value_item_armor_basic:
                player.armor_ad+=self.armor_ad
                player.armor_ap+=self.armor_ap
                player.coins-=self.value_item_armor_basic
                
            else:
                print('ESSE ITEM NÃO ESTÁ DISPONÍVEL NO MOMENTO')

        
        except (ValueError):
            print('DIGITE APENAS UM NUMERO DAS OPÇÕES DISPONÍVEIS.')

        except Exception as e:
            print(f'ERRO DESCONHECIDO: {e}')
