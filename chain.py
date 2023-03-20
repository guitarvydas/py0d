class Chain:
    def __init__ (self, ancestor):
        self.alist = {}
        self.ancestor = ancestor

    def put (self, key, val):
        if (key in self.alist):
            self.alist[key] = [val] + self.alist[key]
        else:
            self.alist[key] = [val]

    def __lookup__ (self, key):
        if (key in self.alist):
            return self.alist[key][0]
        elif self.ancestor:
            return self.ancestor.__lookup__ (key)
        else:
            return None
