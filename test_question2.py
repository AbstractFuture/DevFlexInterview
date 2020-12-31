from question2 import center_zeros


def test_1():
    assert center_zeros([0, 3, 1]) == [3, 0, 1]


def test_2():
    assert center_zeros([1, 1, 3, 0]) == [1, 1, 0, 3]


def test_3():
    assert center_zeros([1, 1, 3, 0, 6, 0]) == [1, 1, 0, 0, 3, 6]


def test_4():
    assert center_zeros([0, 0, 1]) == [0, 0, 1]


def test_5():
    assert center_zeros([]) == []


# Thesis is that to sort these as the instructions describe,
# I need to consider if the zero count is odd or even
# and if the num of non zero elements is odd or even
# New test cases below should confirm


# zero count is 3
# num of non zero elements is 7

#def test_6():
#    assert center_zeros([1, 1, 3, 0, 1, 1, 3, 0, 6, 0]) == [1, 1, 3, 0, 0, 0, 1, 1, 3, 6]

