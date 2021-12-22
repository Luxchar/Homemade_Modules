class graph:
    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self,s):
        if s not in self.adj:
            self.adj[s]=set()

    def ajouter_arc(self,s1,s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)

    def arc(self,s1,s2):
        if s1 not in self.adj:
            return False
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj)

    def voisins(self,s):
        return self.adj[s]

    def degre(self,s):
        return len(self.adj[s])

    def nb_arc(self):
        nb = 0
        for i in range(len(self.adj)):
            if not i in self.adj.keys():
                self.adj[i] = []
                self.adj[i].append(set())
            nb+= self.degre(i)
        return nb

    def supprimer_arcs(self,s1,s2):
        if s2 in self.adj[s1]:
            self.adj[s1].remove(s2)

    def afficher(self):
        for s in self.adj:
            return self.adj

if __name__ == '__main__':
    g = graph()
    g.ajouter_arc(1,2)
    g.ajouter_arc(1,3)
    g.ajouter_arc(3,2)
    g.ajouter_arc(3,6)
    g.ajouter_arc(6,3)

# assert g.afficher() == {1 -> {2,3}, 2 -> set(), 3 -> {2,6}, 4 -> {3}}

#assert g.degre(1) == 1

#assert g.nb_arc() == 5

# assert g.supprimer_arcs(1,2)
# assert g.afficher() == 1 -> {3}


