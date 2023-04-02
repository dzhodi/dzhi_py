from homework1.test3 import find_maximum_and_minimum

r = ["1\n", "3\n", "6\n"]

file1 = open('l.txt', 'w')
file1.writelines(r)
file1.close()


def test_task3():
    assert find_maximum_and_minimum('l.txt') == tuple[1, 6]
