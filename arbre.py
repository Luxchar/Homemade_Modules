class Noeud:
        def __init__(self,d,v,g):
            self.valeur = v
            self.droite = d
            self.gauche = g

        """def affiche(self):
            if self.valeur and self.gauche and self.droite :
                print("(",end ="")
            if self.gauche:
                print("(",end="")
                self.gauche.affiche()
                print(")",end="")
            if self.valeur:
                print(str(self.valeur),end="")
            if self.droite:
                print("(",end="")
                self.droite.affiche()
                print(")",end="")
            if self.valeur and self.gauche and self.droite:
                print(")",end="")"""

        def __eq__(self,z):
            if self.gauche == z.gauche:
                if self.valeur == z.valeur:
                    if self.droite == z.droite:
                        return True
            return False

def affiche(a):
    if a is None:
        return ""
    return "("+affiche(a.gauche)+str(a.valeur)+affiche(a.droite)+")"

c = Noeud(None,"C",None)
b = Noeud(None,"B",c)
d = Noeud(None,"D",None)
a = Noeud(b,"A",d)