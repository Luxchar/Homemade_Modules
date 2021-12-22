class Pile:
    def __init__(self):
        self.contenu = None
        self.taille2 = 0

    def est_vide(self):
        return self.contenu is None

    def empiler(self,v):
        self.contenu = Cellule(v,self.contenu)
        self.taille2 += 1

    def depiler(self):
        if self.est_vide():
            raise IndexError('pile vide')
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v
        self.taille2 -= 1

    def __str__(self):
        if self.contenu is None:
            return ''
        return str(self.contenu)

    def consulter(self):
        c = self.contenu
        while c.suivante is not None:
            c = c.suivante
        return c

    def vide(self):
        self.contenu = None
        self.taille2 = 0

    def taille(self):
        a = 0
        c = self.contenu
        while c.suivante is not None:
            c = c.suivante
            a += 1
        return a+1

class Cellule:
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        if self.suivante == None:
            return str(self.valeur)
        return str(self.valeur) + str(self.suivante.__str__())


