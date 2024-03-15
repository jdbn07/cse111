from water_flow import water_column_height,pressure_gain_from_water_eight
from pytest import approx
import pytest


def test_water_column_height():
    assert water_column_height (0.0,0.0) == (0.0)
    assert water_column_height (0.0,10.0) == (7.5)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_eight(0.0) == approx(0.0, abs=0.001)