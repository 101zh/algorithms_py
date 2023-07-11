class Binary_Search:
    def __init__(self, array, key):
        self.array=array
        self.key=key

    def find(self):
        low=0
        high=self.array.__len__()-1
        while low<=high:
            mid=low+(high-low)//2
            if self.array[mid]<self.key:
                low=mid+1
            elif self.array[mid]>self.key:
                high=mid-1
            else: return mid
        return -1


