class DynamicArray:
 # Created array and initialized with zeros
   
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity

# Returning element at index i
    def get(self, i: int) -> int:
        return self.array[i]


# Saving value to index
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

# Add n at index size
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1



    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_array = [0]*new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
