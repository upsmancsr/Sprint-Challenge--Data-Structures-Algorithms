import unittest
from binary_search_tree import BinarySearchTree

class BinarySearchTreeTests(unittest.TestCase):
  print('---NEW TESTS---')
  def setUp(self):
    self.bst = BinarySearchTree(5)

  def test_depth_first_traversal_1(self):
    print('Test dft 1')
    arr = []
    cb = lambda x: arr.append(x)

    self.bst.depth_first_for_each(cb)

    self.assertEqual(arr, [5])

  def test_depth_first_traversal_2(self):
    print('Test dft 2')
    arr = []
    cb = lambda x: arr.append(x)

    self.bst.insert(2)
    self.bst.insert(3)
    self.bst.insert(7)
    self.bst.insert(9)
    self.bst.depth_first_for_each(cb)

    self.assertEqual(arr, [5, 2, 3, 7, 9])


if __name__ == '__main__':
  unittest.main()