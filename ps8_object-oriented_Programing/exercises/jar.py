class Jar:
  def __init__(self, capacity=12, size=0):
    self.capacity = capacity
    self.size = size

  def __str__(self):
    return f"{"🍪"* self.capacity}"

  def deposit(self, n):
    if self.size + n > self.capacity:
      raise ValueError("Exceeds capacity")
    self.size += n
    return self.size

  def withdraw(self, n):
    if self.size - n < 0:
      raise ValueError("There aren't that many cookies")
    self.size -= n
    return self.size

  @property
  def capacity(self):
    return self._capacity
  
  @capacity.setter
  def capacity(self, capacity):
    if capacity < 0:
      raise ValueError("Capacity must positive integer")
    self._capacity = capacity
  
  @property
  def size(self):
    return self._size
  
  @size.setter
  def size(self, size):
    if not size:
      raise ValueError("Missing size")
    self._size = size

  # @classmethod
  # def get(cls):
  #   capacity = (input("Capacity: "))
  #   size = (input("Size: "))
  #   return cls(capacity, size)
  
def main():
  # jar = Jar.get()
  jar = Jar(15,3)
  print(jar.capacity)


if __name__ == "__main__":
  main()