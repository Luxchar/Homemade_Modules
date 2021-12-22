class Cellule:
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        if self.suivante == None:
            return str(self.valeur)
        return str(self.valeur) + str(self.suivante.__str__())


