#import library
import itertools

#repeat function
def execute_repeat(thing_to_repeat, num_times_to_repeat):
    result = []
    for i in itertools.repeat(thing_to_repeat, num_times_to_repeat):
        result.append(i)
    return result

#slice function
def execute_islice(thing_to_slice, slice_at_location):
    result = []
    for i in itertools.islice(thing_to_slice, slice_at_location):
        result.append(i)
    return result

#cycle function
def execute_cycle(thing_to_cycle, max_cycle_iterations):
    result = []
    count = 0
    for i in itertools.cycle(thing_to_cycle):
        if count > max_cycle_iterations:
            break
        else:
            result.append(i)
            count += 1
    return result

#chain function
def execute_chain(first_thing_to_chain, second_thing_to_chain):
    result = []
    for i in itertools.chain(first_thing_to_chain, second_thing_to_chain):
        result.append(i)
    return result

import unittest

class IWantToTestMyCode(unittest.TestCase):

    #data set
    Cities = ["Lome", "Yaounde", "Djamenna", "Ouagdougou", "Dakar", "Lesotho", "Accra", "Nairobi"]
    MMR = [11, 21, 31, 41, 51, 16, 17, 18] #Maternal Mortality Rate rounded up to the nearst whole number
    MA = ["16", "17", "16", "19", "15", "16", "20", "19"] #Mean age of mother

    def test_repeat(self):
        expected_result = [self.Cities, self.Cities]
        actual_result = execute_repeat(self.Cities, 2)
        self.assertEqual(actual_result, expected_result)
        #raise AssertionError()

    def test_islice(self):
        expected_result = [11, 21, 31, 41, 51, 16, 17]
        actual_result = execute_islice(self.MMR, 7)
        self.assertEqual(actual_result, expected_result)

    def test_cycle(self):
        expected_result = self.Cities + self.Cities
        actual_result = execute_cycle(self.Cities, 15)
        self.assertEqual(actual_result, expected_result)

    def test_chain(self):
        expected_result = self.MMR + self.MA
        actual_result = execute_chain(self.MMR, self.MA)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()