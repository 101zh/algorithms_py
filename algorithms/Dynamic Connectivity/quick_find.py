class QF:
    def __init__(self, n):
        self.id=n*[None]
        for i in range(n):
            self.id[i]=i

    def connected(self, p, q):
        return self.id[p]==self.id[q]

    def union(self, p,q):
        pid=self.id[p]
        qid=self.id[q]
        for i in range(len(self.id)):
            if self.id[i]==pid:
                self.id[i]=qid

