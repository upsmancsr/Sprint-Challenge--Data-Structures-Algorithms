from random import randint

def heapsort(arr):
  heap = Heap() # create a new empty heap
  for i in range(len(arr) - 1): #Loop through input arr and insert each value into the heap
    heap.insert(arr[i]) # insert includes _bubble_up
  
  return heap
 
class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    print('Heap after inserting %(value)s: ' % {"value": value})
    print(self)
    self._bubble_up(len(self.storage) - 1)
    

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2
    print('Heap after bubbling: ')
    print(self)

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2

def gen_random_input(length, max):
  input = []
  for i in range(length):
    input.append(randint(0, max))
  return input

test_length = 10
test_input = gen_random_input(test_length, 100)

test_heap = heapsort(test_input)
print(test_heap[0])

def __str__(self):
      rv = "Heap:\n"

      l = 1
      c = 0

      for i in range(len(self.storage)):
        rv += str(self.storage[i]) + "  "

        c += 1

        if c >= l:
          rv += "\n" + "  " * l
          c = 0
          l *= 2

      rv += "\n"

      return rv