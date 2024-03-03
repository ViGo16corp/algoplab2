import unittest
from triplet_sum import find_triplet_sum

class TestFindTripletSum(unittest.TestCase):
    def test_example(self):
        # Перевірка на прикладі
        arr = [1, 2, 3]
        target = 6
        self.assertTrue(find_triplet_sum(arr, target))

    def test_negative_example(self):
        # Перевірка на прикладі, коли таких чисел немає
        arr = [1, 2, 3]
        target = 10
        self.assertFalse(find_triplet_sum(arr, target))

if __name__ == "__main__":
    unittest.main()