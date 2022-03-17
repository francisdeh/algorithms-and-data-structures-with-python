import unittest
from selection_sort import selection_sort, smallest_element_index


class SelectionSortTest(unittest.TestCase):
    def setUp(self) -> None:
        self.original_list = [11, 42, 71, 3, 98, 35, 12, 54, 96, 68, 74, 66, 80, 83, 76, 94, 90, 22, 91]
        self.sorted_list = [3, 11, 12, 22, 35, 42, 54, 66, 68, 71, 74, 76, 80, 83, 90, 91, 94, 96, 98]
        self.smallest_element = 3

    def test_smallest_element(self):
        sm_element_index = smallest_element_index(self.original_list)
        self.assertEqual(self.smallest_element, self.original_list[sm_element_index], "Smallest element index is not returned")

    def test_selection_sorted_list(self):
        sorted_lst = selection_sort(self.original_list)
        self.assertListEqual(self.sorted_list, sorted_lst, "Sorted lists not the same")
