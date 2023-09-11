import pytest

from src.analogy.core.confidence_interval import (
    ByarsConfidenceInterval,
    ChiSquaredConfidenceInterval,
)


def test_byars_confidence_interval():
    ci = ByarsConfidenceInterval(65, 100)

    lower = ci.lower_bound() * 100
    upper = ci.upper_bound() * 100

    assert round(lower, 4) == 50.1632
    assert round(upper, 4) == 82.8491


def test_chi_confidence_interval():
    ci = ChiSquaredConfidenceInterval(65, 100)

    lower = ci.lower_bound() * 100
    upper = ci.upper_bound() * 100

    assert round(lower, 4) == 50.1656
    assert round(upper, 4) == 82.8478
