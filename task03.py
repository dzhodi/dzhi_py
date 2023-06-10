class Filter:

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):

        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):

    filter_funcs = []
    for key, value in keywords.items():
        def keyword_filter_func(item):
            return item.get(key) == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


# Tests
def test_filter():
    # Test for empty data
    assert make_filter(name='polly').apply([]) == []

    # Test for no match
    assert make_filter(name='polly').apply([{'name': 'John'}, {'name': 'Mary'}]) == []

    # Test for single match
    assert make_filter(name='polly').apply([{'name': 'John'}, {'name': 'polly'}]) == [{'name': 'polly'}]

    # Test for multiple matches
    assert make_filter(type='bird').apply(sample_data) == [
        {'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}]

    # Test for incorrect keyword
    assert make_filter(age=30).apply([{'name': 'John', 'age': 25}, {'name': 'Mary', 'age': 35}]) == []

    # Test for incorrect value
    assert make_filter(name='polly', type='dog').apply(sample_data) == []


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]

test_filter()