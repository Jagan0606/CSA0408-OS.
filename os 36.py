# linked_allocation_sim.py
# Each block points to next block id (or None). Directory stores first and last.
class Node:
    def __init__(self, data, next_idx=None):
        self.data = data
        self.next = next_idx

class LinkedFile:
    def __init__(self, blocks):  # blocks: list of Node
        self.blocks = blocks
        self.head = 0 if blocks else None
        self.tail = len(blocks)-1 if blocks else None

    def read_all(self):
        idx = self.head
        while idx is not None:
            print(f"Block {idx}: {self.blocks[idx].data}")
            idx = self.blocks[idx].next

if __name__ == "__main__":
    b = [Node("data0", 1), Node("data1", 3), Node("data2", None), Node("data3", 2)]
    # This example has a small arbitrary linking; typical linked list would be sequential
    # Let's make a simple chain:
    b = [Node("data0", 1), Node("data1", 2), Node("data2", None)]
    lf = LinkedFile(b)
    lf.read_all()
