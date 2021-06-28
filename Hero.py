class Hero():
    """英雄父类"""
    hp=0
    power=0
    name=" "
    lines=" "

    def fight(self,enemy_hp,enemy_power):
        my_final_hp=self.hp-enemy_power
        enemy_final_hp=enemy_hp-self.power
        if my_final_hp>enemy_final_hp:
            print(f"{self.name}赢了")
        elif my_final_hp<enemy_final_hp:
            print("敌人赢了")
        else:
            print("我们打平了")
    def speak_lines(self):
        print(self.name+":"+ self.lines)