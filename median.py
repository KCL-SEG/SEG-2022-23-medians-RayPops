"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numbers):
    """Return the median of the given list of numbers."""
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(median(numbers))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
