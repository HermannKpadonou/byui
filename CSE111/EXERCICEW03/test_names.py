from names import make_full_name, extract_family_name, extract_given_name

import pytest


def test_make_full_name():
    """Test the make_full_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    
def test_extract_family_name():
    """Test the extract_family_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_family_name("Brown; Sally") == "Brown"
    
def test_extract_given_name():
    """Test the extract_given_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_given_name("Brown; Sally") == "Sally"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
    