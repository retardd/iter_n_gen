import types


def flat_generator(list_of_lists):
    for list_items in list_of_lists:
        i = 0
        while i < len(list_items):
            item = list_items[i]
            while type(item) is list:
                list_items = list_items[:i] + item + list_items[i + 1:]
                if i >= len(list_items):
                    break
                item = list_items[i]
            if i >= len(list_items):
                break
            i += 1
            yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()