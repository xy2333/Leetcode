class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
        	self.d.add(val)
        	return True
        else:
        	return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
        	self.d.remove(val)
        	return True
        else:
        	return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        a = random.randint(0,len(self.d))
        res = list(self.d)
        return res[a]


        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)

param_3 = obj.getRandom()
print(param_3)