import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.num = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        try:
            self.index[val].append(len(self.num))
        except KeyError:
            self.index[val] = []
            self.index[val].append(len(self.num))
        self.num.append(val)
        return len(self.index[val]) == 1  # if this insert operation is the first operation of this val


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        try:
            if len(self.index[val]) == 0:
                return False
            else:
                delete_index = self.index[val].pop()
                last_val = self.num.pop()
                last_val_index = len(self.num)

                if delete_index != last_val_index:
                    self.index[last_val].remove(last_val_index)
                    self.index[last_val].append(delete_index)

                    self.num[delete_index] = last_val

                return True
        except KeyError:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.num)


obj = RandomizedCollection()
param_11 = obj.insert(1)
param_12 = obj.insert(1)
param_13 = obj.insert(2)
param_21 = obj.insert(2)
param_22 = obj.insert(2)
param_5 = obj.remove(1)
param_51 = obj.remove(1)
param_52 = obj.remove(2)
param_53 = obj.insert(1)
param_54 = obj.remove(2)
param_6 = obj.getRandom()

