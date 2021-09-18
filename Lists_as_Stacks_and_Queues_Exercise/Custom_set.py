class CustomSet:
    resize_factor = 0.7

    def __init__(self):
        self.count = 0
        self.capacity = 8
        self.values = [None] * self.capacity

    def execute_resize_check(self):
        return self.capacity * self.resize_factor <= self.count

    # the below function  resizes the set
    def resize(self):
        old_values = self.values
        self.count = 0
        self.capacity *= 2
        self.values = [None] * self.capacity
        for nested_list in old_values:
            if nested_list:
                for value in nested_list:
                    self.add(value)

    def get_index(self, value):
        value_hash = hash(value)
        return abs(value_hash) % self.capacity

    def add(self, value):
        #  do the below to be sure that the valie will be in range from 0 to capacity
        index = self.get_index(value)
        if not self.values[index]:
            self.values[index] = []

        if value not in self.values[index]:
            self.values[index].append(value)
            self.count += 1

            # the below statement checks if its needed to resize the set, example from 8 Nones to 16 etc
        if self.execute_resize_check():
            self.resize()

    def remove(self, value):
        if not self.contains(value):
            return

        index = self.get_index(value)
        self.values[index].remove(value)
        self.count -= 1

    def contains(self, value):
        index = self.get_index(value)
        if not self.values[index]:
            return False

        if value not in self.values[index]:
            return False

        return True

    def __contains__(self, item):
        return self.contains(item)


ss = CustomSet()

values = [0, 1, -1, 0, 3.14, 'Pesho', 'Stamat']
print(len(values))
for x in values:
    ss.add(x)
    print(x, hash(x))

print(ss.values)

# 10^6 Log(2)10^6 ~ 20 That means that we add 1 billion elements with 30 resizes
