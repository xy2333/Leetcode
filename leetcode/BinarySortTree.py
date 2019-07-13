class BinTNode(object):
    """docstring for BinTNode"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class AVLNode(BinTNode):
    """docstring for AVLNode"""
    def __init__(self, data):
        BinTNode.__init__(self,data)        
        self.bf = 0

class BinarySortTree():
    """docstring for BinarySortTree"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def insert(self, data):
        bt = self._root
        if bt is None:
            self._root = BinTNode(data)
            return
        while 1:
            if bt.data > data:
                if bt.left is None:
                    bt.left = BinTNode(data)
                    return
                bt = bt.left
            elif bt.data < data:
                if bt.right is None:
                    bt.right = BinTNode(data)
                    return
                bt = bt.right
            else:
                return

    def delete(self, data):
        p = None
        q = self._root
        while q is not None and q.data != data:
            if q.data > data:
                p, q = q, q.left
            else:
                p, q = q, q.right
        if q is None:
            return
        if q.left is None:
            if p is None:
                self._root = q.right
            else:
                if q is p.left:
                    p.left = q.right
                else:
                    p.right = q.right
            return
        maxleft = q.left
        while maxleft.right is not None:
            maxleft = maxleft.right
        if p is None:
            self._root = q.left
        else:
            if q is p.left:
                p.left = q.left
            else:
                p.right = q.left
        maxleft.right = q.right
        return

    def Print(self):
        # write code here
        deque = []
        res = [[]]
        nowlevel = 0
        nextlevel = 0
        if self._root is None:
            return []
        deque.append(self._root)
        nowlevel += 1
        while len(deque) > 0:
            temp = deque.pop(0)
            nowlevel -= 1
            res[-1].append(temp.data)
            if temp.left is not None:
                deque.append(temp.left)
                nextlevel += 1
            if temp.right is not None:
                deque.append(temp.right)
                nextlevel += 1
            if nowlevel == 0:
                nowlevel, nextlevel = nextlevel, nowlevel
                if nowlevel != 0:
                    res.append([])
        return res

class AVL(BinarySortTree):
    """docstring for AVL"""
    def __init__(self):
        BinarySortTree.__init__(self)      

    def LL(self,a,b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    def RR(self,a,b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    def LR(self,a,b):
        c = b.right
        b.right,a.left = c.left,c.right
        c.right,c.left = a,b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            b.bf = 0
            a.bf = -1
        else:
            b.bf = 1
            a.bf = 0
        c.bf = 0
        return c

    def RL(self,a,b):
        c = b.left
        a.right,b.left = c.left,c.right
        c.left,c.right = a,b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            b.bf = 0
            a.bf = 1
        c.bf = 0
        return c

    def insert(self,data):
        a = p =self._root
        if a is None:
            self._root = AVLNode(data)
            return
        pa = q = None
        while p is not None:
            if data == p.data:
                return
            if p.bf != 0:
                a,pa = p,q
            if p.data > data:
                q = p
                p = p.left
            else:
                q = p
                p = p.right
        if data > q.data:
            q.right = AVLNode(data)
        else:
            q.left = AVLNode(data)

        if data > a.data:
            p = b = a.right
            d = -1
        else:
            p = b = a.left
            d = 1
        while p.data != data:
            if p.data > data:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right
        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:
            a.bf = 0
            return
        if d == 1:
            if b.bf == 1:
                b = self.LL(a,b)
            else:
                b = self.LR(a,b)
        else:
            if b.bf == -1:
                b = self.RR(a,b)
            else:
                b = self.RL(a,b)
        if pa is None:
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b

# t = BinarySortTree()
# t.insert(5)
# t.insert(4)
# t.insert(6)
# t.insert(3)
# t.insert(10)
# t.insert(7)
# t.insert(2)
# t.insert(1)
# a = t.Print()
# print(a)
# print('************************')
# t.delete(6)
# t.delete(5)
# t.delete(7)
# a = t.Print()
# print(a)

t = AVL()
t.insert(5)
t.insert(4)
t.insert(6)
t.insert(3)
t.insert(10)
t.insert(7)
t.insert(2)
t.insert(1)
a = t.Print()
print(a)