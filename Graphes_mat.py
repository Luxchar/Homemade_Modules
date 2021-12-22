class Graphe_mat:
    def __init__(self,n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]

    def ajouter_arc(self,s1,s2):
        self.adj[s1][s2] = True

    def arc(self,s1,s2):
        return self.adj[s1][s2]

    def voisins(self,s):
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append[i]
        return v

    def afficher(self):
        for i in range(self.n):
            print(s,'->',end='')
            for s in range(self.n):
                print(i,end='')
            print()

    def afficher2(self,s):
        for i in range(self.n):
            if self.adj[s][i]:
                print(s,":",i)

    def nb_sommets(self):
        nb = 0
        for i in range(self.n):
            if self.adj[i] is not None:
                nb += 1
        return nb

    def degre(self,s):
        adj_sommet =  self.adj[s]
        degree = len(adj_sommet) + adj_sommet.count(s)
        return degree

    def nb_arc(self):
        nbr = 0
        for i in range(self.n):
            degre = self.degre(i)
            nbr += degre
        return nbr


g = Graphe_mat(3)
g.ajouter_arc(1,0)
g.ajouter_arc(1,2)
g.ajouter_arc(0,2)

# assert g.afficher(1) == 1 : 0, 1 : 2

# assert g.nb_sommet() == 3

#assert g.degre(2) == 3

#assert g.nb_arc() == 14