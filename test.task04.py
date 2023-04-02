from homework1.test4 import check_sum_of_four


def test_task4():
    assert check_sum_of_four([-8, 8, 8, 5], [7, 3, -2, -9], [2, -1, 0, -9], [0, 4, 5, 3]) == 6
