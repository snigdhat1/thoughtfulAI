import pytest
from sort import sort


# Format: (width, height, length, mass, expected_result)
test_cases = [
    # REJECTED (bulky and heavy)
    (200, 100, 100, 25, "REJECTED"),
    (160, 50, 60, 30, "REJECTED"),
    (100, 160, 70, 21, "REJECTED"),
    (100, 100, 100, 20, "REJECTED"),
    (150, 150, 150, 20, "REJECTED"),
    (1000, 1000, 1000, 1000, "REJECTED"),

    # SPECIAL (bulky only)
    (200, 50, 10, 10, "SPECIAL"),
    (150, 150, 150, 15, "SPECIAL"),
    (150, 15, 15, 15, "SPECIAL"),
    (15, 150, 15, 15, "SPECIAL"),
    (15, 15, 150, 15, "SPECIAL"),
    (1000, 1000, 1, 0.1, "SPECIAL"),

    # SPECIAL (heavy only)
    (10, 10, 10, 25, "SPECIAL"),
    (50, 50, 30, 21, "SPECIAL"),
    (50, 50, 30, 20, "SPECIAL"),

    # Edge cases
    (149, 149, 149, 19.9, "SPECIAL"),
    (33, 39, 819, 19.99, "SPECIAL"),
    (100, 100, 100, 19.9, "SPECIAL"),

    # STANDARD (not bulky, not heavy)
    (10, 10, 10, 5, "STANDARD"),
    (40, 50, 60, 10, "STANDARD"),
    (100, 100, 99, 19, "STANDARD"),
    (0, 0, 0, 0, "STANDARD"),
    (1, 1, 1, 19.9, "STANDARD"),
    (149.9, 1, 1, 19.9, "STANDARD"),
]

@pytest.mark.parametrize("width, height, length, mass, expected", test_cases)
def test_sort_packages(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected