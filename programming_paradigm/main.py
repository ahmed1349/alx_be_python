
import sys
from robust_division_calculator import safe_divide

def main():
    # Ensure exactly two arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get the command-line arguments for numerator and denominator
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call safe_divide and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
