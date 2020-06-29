class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.number_of_vals = 0
        self.list = []

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        else:
            self.list[self.number_of_vals % (self.capacity)] = item
        # each time the total number of values that have been passed in will increase
        # therefore each time the index of which item is going to replace will alternate by one each time
        # because modulo is being used to determine the remainder which also determines the oldest value.
        
        self.number_of_vals += 1
        # each time the number of values increases regardless

    def get(self):
        return self.list