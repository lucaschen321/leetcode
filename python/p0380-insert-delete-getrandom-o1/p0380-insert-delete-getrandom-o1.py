import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.values_to_index:
            self.values.append(val)
            self.values_to_index[val] = len(self.values) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        [1:4, 2:5]
        """
        if val in self.values_to_index:
            last_value = self.values[-1]
            deleted_value_index = self.values_to_index[val]

            self.values[deleted_value_index] = last_value
            self.values_to_index[last_value] = deleted_value_index

            del self.values_to_index[val]
            self.values.pop()

            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.values[random.randint(0, len(self.values) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
