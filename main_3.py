class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.low_i = 0
        self.high_i = 0
        self.temp_list = self.list_of_list[self.low_i]
        return self

    def __next__(self):
        if self.high_i >= len(self.temp_list):
            self.low_i += 1
            if self.low_i >= len(self.list_of_list):
                raise StopIteration
            self.temp_list = self.list_of_list[self.low_i]
            self.high_i = 0
        else:
            while self.temp_list and type(self.temp_list[self.high_i]) is list:
                self.temp_list = self.temp_list[:self.high_i] + self.temp_list[self.high_i] + self.temp_list[self.high_i + 1:]
        self.high_i += 1
        return self.temp_list[self.high_i - 1]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()