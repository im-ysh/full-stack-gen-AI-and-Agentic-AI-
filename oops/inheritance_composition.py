class BaseChai:
    def __init__(self,type_,):
        self.type = type_
        
    def prepare(self):
        print(f"preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding cardamom, ginger, cloves")

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"serving {self.chai.type} chai in the shop")
        self.chai = self.chai_cls("Regular")

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()