class Noeud:
    def __init__(self,g,v,d):
        self.gauche = g
        self.droit = d
        self.valeur = v

class ABR:
    def __init__(self):
        self.racine = None

    def est_vide(self):
        return self.racine is None

    def ajouter(self,x):
        self.racine = ajoute(x,self)

    def contient(self,x):
        return appartient(x,self.racine)

    def minimum(self,a):
        if a is None:
            return None
        if self.racine.gauche is None:
            return self.racine.valeur
        return minimum(self.racine.gauche)

    def __str__(self):
        return str(self.racine)

    def compter(self):
        return compte(x,a)

occ = 0

#Ex 31
def compte(x,a):
    global occ
    if a == None:
        return occ
    elif x > a.valeur:
        return compte(x,a.droit)
    elif x < a.valeur:
        return compte(x,a.gauche)
    else:
        occ += 1
        return compte(x,a.gauche)

#Ex 30
def ajouter(x,a):
    if a is None:
        return Noeud(None,x,None)
    if x < a.valeur:
        return Noeud(ajouter(x,a.gauche), a.valeur, a.droit)
    if x > a.valeur:
        return Noeud(a.gauche,a.valeur,ajouter(x,a.droit))

#Ex 32
def remplir(a,t):
    if a is not None:
        remplir(a.gauche,t)
        t.append(a.valeur)
        remplir(a.droit,t)
    return t

#Ex 33
def trier(t):
    arbre = ABR()
    while t != []:
        ajouter(t[0],arbre.racine)
        t = t[1:]
    return str(arbre), str(t)



def taille(a):
    if a is None:
        return 0
    return 1+taille(a.droit+taille(a.gauche))

def hauteur(a):
    if a is None:
        return 0
    return 1+max(hauteur(a.gauche),hauteur(a.droit))

def infixe(a):
    if a is None:
        return None
    infixe(a.gauche)
    print(a.valeur)
    infixe(a.droit)

def prefixe(a):
    if a is None:
        return None
    print(a.valeur)
    prefixe(a.gauche)
    prefixe(a.droit)

def suffixe(a):
    if a is None:
        return None
    suffixe(a.gauche)
    suffixe(a.droit)
    print(a.valeur)

def appartient_a(x,a):
    if a is None:
        return False
    if x < a.valeur:
        return appartient_a(x,a.gauche)
    if x > a.valeur:
        return appartient_a(x,a.droit)
    else:
        return True  # x = a.valeur

test = Noeud(None,2,Noeud(None,3,None))
tab = [1,2,3]


