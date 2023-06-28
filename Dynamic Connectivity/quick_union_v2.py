class QUI:
    def __init__(self, n):
        self.id=n*[None]
        self.sz=n*[1]
        for i in range(n):
            self.id[i]=i

    def root(self, i):
        
        while self.id[i]!=i:
            id[i]=id[id[i]]
            i=self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p)==self.root(q)

    def union(self, p,q):
        rootP=self.root(p)
        rootQ=self.root(q)
        if self.sz[rootP]<self.sz[rootQ]:
            self.id[rootP]=self.id[rootQ]
            self.sz[rootQ]+=self.sz[rootP]
        else:
            self.id[rootQ]=self.id[rootP]
            self.sz[rootP]+=self.sz[rootQ]

