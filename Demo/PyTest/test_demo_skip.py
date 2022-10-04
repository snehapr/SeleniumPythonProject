import pytest
import sys

# This will skip the test_demo_1 function
# we can also give the reason in this skip test
# And to print the reason along with the skip test result, we need to be using the
# -rxs flag when we are trying to run the test from the command line
# like 'pytest -v -rxs'


@pytest.mark.skip(reason="Not included in this build")
@pytest.mark.demo
def test_demo_1():
    assert True

# we are making use of the skipif method of pytest which executes the function only when
# the condition holds true


@pytest.mark.skipif(sys.version_info < (3,6), reason = "requires python 3.6 or higher")
@pytest.mark.demo
def test_demo_2():
    assert True

# when we want to run the specific function in the pytest, then we can make use of -k flag
# in the command line as follows
# 'pytest test_demo_skip.py -v -rxs -k demo_3'
# In the above case, the first 2 functions demo_1 and demo_2 will be deselected
# And only demo_3 function will be run


@pytest.mark.demo
def test_demo_3():
    assert True

# instead of using the -k flag in the terminal and running the separate tests ,
# we can make use of this mark.<any_name> in pytest where it used to give to give a name to
# the function
# In the command line we can use the command 'pytest filename.py -m <name_of_the_function>'


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True


