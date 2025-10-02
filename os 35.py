# indexed_allocation_sim.py
# Simulate index block: index[i] -> block content
class IndexedFile:
    def __init__(self, blocks):
        # blocks is a list representing blocks of file
        self.index_block = list(range(len(blocks)))  # store indices
        self.blocks = blocks

    def read_block(self, i):
        if i < 0 or i >= len(self.index_block):
            raise IndexError("Block index out of range")
        block_id = self.index_block[i]
        print(f"Index entry {i} -> block {block_id}: {self.blocks[block_id]}")
        return self.blocks[block_id]

if __name__ == "__main__":
    blocks = ["B0 data", "B1 data", "B2 data", "B3 data"]
    f = IndexedFile(blocks)
    f.read_block(2)
