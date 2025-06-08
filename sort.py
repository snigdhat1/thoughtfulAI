##### CHANGE BACK TO SORT
def sort_packages(width, height, length, mass) -> str:
    volume = width * height * length
    bulky = False
    heavy = False
    if volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150:
        bulky = True
    ##### CHANGE BACK TO SORT
    if mass >= 20:
        heavy = True
   
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
##### CHANGE BACK TO SORT


if __name__ == "__main__":
    # Format: (width, height, length, mass)
    test_cases = [
        # REJECTED (bulky and heavy)
        (200, 100, 100, 25),
        (160, 50, 60, 30),
        (100, 160, 70, 21),
        # Edge casees
        (100,100,100,20),
        (150, 150, 150, 20),
        (1000, 1000, 1000, 1000),


        # SPECIAL (bulky only)
        (200, 50, 10, 10),
        (100, 200, 30, 10),
        (80, 80, 200, 15),
        # edge case
        (150, 150, 150, 15),
        (150, 15, 15, 15),
        (15, 150, 15, 15),
        (15, 15, 150, 15),
        (1000, 1000, 1, 0.1),


        # SPECIAL (heavy only)
        (10, 10, 10, 25),
        (50, 50, 30, 21),
        (50, 50, 30, 20),

        # edge case
        (149,149,149,19.9),
        (33, 39, 819, 19.99),

        # STANDARD (not bulky, not heavy)
        (10, 10, 10, 5),
        (40, 50, 60, 10),
        (100, 100, 99, 19),
        (0, 0, 0, 0),
        (1,1,1,19.9),
    ]
    for width, height, length, mass in test_cases:
        result = sort_packages(width, height, length, mass)
        volume = width * height * length
        print(f"Input: ({width}, {height}, {length}, {mass}) → Result: {result}")