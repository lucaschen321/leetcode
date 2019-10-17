from collections import defaultdict
import random


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.values_to_indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.values.append(val)
        if val not in self.values_to_indices:
            self.values_to_indices[val].add(len(self.values) - 1)
            return True
        else:
            self.values_to_indices[val].add(len(self.values) - 1)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.values_to_indices[val]:
            last_value = self.values[-1]
            deleted_index = self.values_to_indices[val].pop()

            self.values[deleted_index] = last_value
            self.values_to_indices[last_value].add(deleted_index)
            self.values_to_indices[last_value].remove(len(self.values) - 1)

            self.values.pop()

            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.values)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
