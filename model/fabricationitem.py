class FabricationItem:

    def __init__(self="", id="", email="", design="", cost="", time="", machinist="", stage=""):
        self.id = id
        self.email = email
        self.design = design
        self.cost = cost
        self.time = time
        self.machinist = machinist
        self.stage = stage

    def toJson(self):
        return {
            'id': self.id,
            'email': self.email,
            'design': self.design,
            'cost': self.cost,
            'time': self.time,
            'machinist': self.machinist,
            'stage': self.stage
        }