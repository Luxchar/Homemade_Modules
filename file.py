class Cellule:
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        a = self
        test = ""
        while a is not None:
            test = test + str(a.valeur) + " "
            a = a.suivante
        return test


class File:

    def __init__(self):
        self.contenu = None

    def est_vide(self):
        return self.contenu == None

    def renverser(self,l1):
        c = l1
        r = None
        while c is not None:
            r = Cellule(c.valeur,r)
            c = c.suivante
        return r

    def empiler(self,v):
        self.contenu = Cellule(v,self.contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("pile vide")
        v = self.renverser(self.contenu)
        resultat = v.valeur
        self.contenu = self.renverser(v.suivante)
        return resultat

    def __str__(self):
        if self.contenu is None:
            return ""
        return str(self.contenu)


a = File()
a.empiler("1")
a.empiler("2")
a.empiler("3")

print(a.depiler())