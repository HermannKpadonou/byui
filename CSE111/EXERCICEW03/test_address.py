from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Test the extract_city function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_city("123 Main St, Springfield, IL 62701") == "Springfield"
    assert extract_city("456 Elm St, Shelbyville, IN 46176") == "Shelbyville"
    assert extract_city("789 Oak St, Capital City, CA 90210") == "Capital City"
    assert extract_city("101 Pine St, Smalltown, TX 75001") == "Smalltown"

def test_extract_state():
    """Test the extract_state function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_state("123 Main St, Springfield, IL 62701") == "IL"
    assert extract_state("456 Elm St, Shelbyville, IN 46176") == "IN"
    assert extract_state("789 Oak St, Capital City, CA 90210") == "CA"
    assert extract_state("101 Pine St, Smalltown, TX 75001") == "TX"

def test_extract_zipcode():
    """Test the extract_zipcode function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_zipcode("123 Main St, Springfield, IL 62701") == "62701"
    assert extract_zipcode("456 Elm St, Shelbyville, IN 46176") == "46176"
    assert extract_zipcode("789 Oak St, Capital City, CA 90210") == "90210"
    assert extract_zipcode("101 Pine St, Smalltown, TX 75001") == "75001"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])