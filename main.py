from enum import Enum


class Lion:
    def __init__(self,state):
        if state.upper()=="ГОЛОДНЫЙ":
            self.state="ГОЛОДНЫЙ";
        else:
            self.state="СЫТЫЙ";
    def input(self,obj):
        if self.state=="СЫТЫЙ":
            if obj.upper()=="АНТИЛОПА":
                self.action="Спать";
            elif obj.upper()=="ОХОТНИК":
                self.action="Убежать";
            elif obj.upper()=="ДЕРЕВО":
                self.action="Смотреть";
            else:
                return "Неверный символ";
            self.state="ГОЛОДНЫЙ";
        elif self.state=="ГОЛОДНЫЙ":
            if obj.upper()=="АНТИЛОПА":
                self.action="Съесть";
                self.state="СЫТЫЙ";
            elif obj.upper()=="ОХОТНИК":
                self.action="Убежать";
            elif obj.upper()=="ДЕРЕВО":
                self.action="Спать";
            else:
                return "Неверный символ";