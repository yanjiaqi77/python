from Police import Police
from Timo import Timo


class HeroFactory():
    def creat_hero(self,name):
        if name == "Police" or name=="police":
            return Police()
        elif name =="Timo" or name=="timo":
            return Timo()
        else:
            raise Exception('抱歉，英雄列表中暂无您所选英雄')

herofactory=HeroFactory()
police=herofactory.creat_hero("police")
timo=herofactory.creat_hero("timo")
police.speak_lines()
timo.speak_lines()
police.fight(timo.hp,timo.power)
timo.fight(police.hp,police.power)