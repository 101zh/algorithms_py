class QUI:
    def __init__(self, n):
        self.id=n*[None]
        self.sz=n*[1]
        for i in range(n):
            self.id[i]=i

    def root(self, p):
        root=p
        while self.id[root]!=root:
            root=self.id[root]
            
        while p!=root:
            parent=id[p]
            id[p]=root
            p=parent

        return root

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

