class QUI:
    def __init__(self, n):
        self.id=n*[None]
        self.sz=n*[1]
        for i in range(n):
            self.id[i]=i

    def root(self, x):
        while self.id[x]!=x:
            x=self.id[x]
        return x

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
