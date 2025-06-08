import sys

def sort(width, height, length, mass) -> str:
    volume = width * height * length
    bulky = False
    heavy = False
    if volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150:
        bulky = True

    if mass >= 20:
        heavy = True
   
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"



if __name__ == "__main__":
    # Takes in 4 command line arguements

    if len(sys.argv) != 5:
        print("Usage: python sort.py <width> <height> <length> <mass>")
        sys.exit(1)

    width = float(sys.argv[1])
    height = float(sys.argv[2])
    length = float(sys.argv[3])
    mass = float(sys.argv[4])

    result = sort(width, height, length, mass)
    print(f"Classification: {result}")