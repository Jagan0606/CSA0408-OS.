# contiguous_allocation_sim.py
# Simulate a simple contiguous file where records are stored one after another.
# To access record i we simulate reading from 0..i.

class ContiguousFile:
    def __init__(self, records):
        self.records = list(records)

    def read_record(self, index):
        if index < 0 or index >= len(self.records):
            raise IndexError("Record out of range")
        # simulate reading all previous records
        for i in range(index + 1):
            print(f"Reading record {i}: {self.records[i]}")
        return self.records[index]

if __name__ == "__main__":
    f = ContiguousFile(["r0", "r1", "r2", "r3", "r4"])
    print("Access record 3:")
    f.read_record(3)
