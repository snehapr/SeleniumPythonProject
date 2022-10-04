import pytest

def sum(a,b):
    return a+b


# Instead of reusing the same code several times, we can parametrize the variables to avoid
# the redundancy of the code

# With parametrization we make use of this below annotation and by giving the series of
# inputs and the output values which we want to obtain

@pytest.mark.parametrize("input1, input2, output",
                         [
                             (2,3,5),
                             (3,3,6),
                             (5,5,10)
                         ])
def test_calc_sum_1(input1, input2, output):
    result = sum(input1, input2)
    assert result == output



# Without parametrization the below code holds good

# def test_calc_sum_1():
#     result = sum(2,3)
#     assert result == 5
#

# def test_calc_sum_2():
#     result = sum(3,3)
#     assert result == 6
#
#
# def test_calc_sum_3():
#     result = sum(5,5)
#     assert result == 10