class Actor:
    def __init__(self, name):
        self.name = name
        self.abilities = {}

    def can(self, ability):
        self.abilities[type(ability)] = ability

    def ability_to(self, ability_cls):
        return self.abilities[ability_cls]
