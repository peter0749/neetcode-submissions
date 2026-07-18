class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._curr_size = 0
        self._data = [None] * self._capacity

    def get(self, i: int) -> int:
        return self._data[i]

    def set(self, i: int, n: int) -> None:
        self._data[i] = n

    def pushback(self, n: int) -> None:
        if self._curr_size == self._capacity:
            self.resize()
        self._data[self._curr_size] = n
        self._curr_size += 1

    def popback(self) -> int:
        self._curr_size -= 1
        return self._data[self._curr_size]

    def resize(self) -> None:
        self._data.extend([None] * self._capacity)
        self._capacity *= 2

    def getSize(self) -> int:
        return self._curr_size
    
    def getCapacity(self) -> int:
        return self._capacity
