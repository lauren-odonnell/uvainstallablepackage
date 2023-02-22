import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)
    
def test_success_string():
    test_str = "this is a test string"

    assert "THIS IS A TEST STRING" == sh.caps_string(test_str), "String <{}> not cleaned as expected".format(test_str)

@pytest.mark.skip(reason="no way of currently testing this")
def test_fail_string():
    test_str = " T h i s !  i s             a   , t e s t   s t r i n g     "

    assert "T h i s   i s   a   t e s t   s t r i n g " == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)
    
@pytest.mark.skipif(sys.platform == 'darwin', reason="incorrect OS")
def test_skipif():
    test_str = " T h i s !  i s             a   , t e s t   s t r i n g     "
    print("My platform is", sys.platform)

    assert "T h i s   i s   a   t e s t   s t r i n g " == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

