class QU:
    def __init__(self, n):
        self.id=n*[None]
        for i in range(n):
            self.id[i]=i

    def findRoot(self, x):
        while self.id[x]!=x:
            x=self.id[x]
        return x

    def connected(self, p, q):
        return self.findRoot(p)==self.findRoot(q)

    def union(self, p,q):
        self.id[self.findRoot(p)]=self.findRoot(q)
