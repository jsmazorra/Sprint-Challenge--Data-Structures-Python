class RingBuffer:
    # A class for fixed-size buffers.
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.index = 0

    def append(self, item):
        # The append method adds the given element to the buffer.
        self.storage[self.index] = item
        self.index = (self.index + 1) % len(self.storage)

    def get(self):
        # The get method returns all of the elements in the buffer in a list in
        # their given order. It should not return any None values in the list
        # even if they are present in the ring buffer.
        return [item for item in self.storage if item is not None]
