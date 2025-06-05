from names import make_full_name, extract_family_name, extract_given_name
import pytest
from pytest import approx

def test_make_full_name():
    """Test the make_full_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Alice", "Smith") == "Smith; Alice"
    assert make_full_name("Bob", "Johnson") == "Johnson; Bob"

def test_extract_family_name():
    """Test the extract_family_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith; Alice") == "Smith"
    assert extract_family_name("Johnson; Bob") == "Johnson"

def test_extract_given_name():
    """Test the extract_given_name function by calling it and
    comparing the values it returns to the expected values.
    """
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Smith; Alice") == "Alice"
    assert extract_given_name("Johnson; Bob") == "Bob"