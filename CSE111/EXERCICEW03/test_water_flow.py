from water_flow import water_column_height, pressure_gain_from_water_height
from pytest import approx
import pytest

def test_water_column_height():
    """Test the water_column_height function by calling it and
    comparing the values it returns to the expected values.
    """
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    """Test the pressure_gain_from_water_height function by calling it and
    comparing the values it returns to the expected values.
    """
    assert pressure_gain_from_water_height(0.0) == approx(0.0)
    assert pressure_gain_from_water_height(7.5) == approx(73.5)
    assert pressure_gain_from_water_height(25.0) == approx(245.25)
    


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])