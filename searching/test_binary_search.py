import unittest
from binary_search import binary_search


class BinarySearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.elements = [x + 1 for x in range(10)]

    def test_binary_search_returns_index_of_element(self):
        actual_position = 6
        binary_search_position = binary_search(self.elements, 7)
        self.assertEqual(actual_position, binary_search_position, "Element not found in right position")

    def test_binary_search_returns_none_for_element(self):
        binary_search_position = binary_search(self.elements, 17)
        self.assertIsNone(binary_search_position, "Element position is not none")

