import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    count = 0
    with open(filepath, 'r') as infile:
        for line in infile:
            count += 1
            values = line.strip().split("\t")
            try:
                number = float(values[column])
                if math .isnan(number):
                    continue
                numbers.append(number)
                
            except ValueError:
                continue
            except IndexError:
                raise
    return numbers, count

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    return float(sum(numbers) / len(numbers))


def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    return (max(numbers), min(numbers))

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    if len(numbers) <= 1:
        return 0.0
    average = calculate_average(numbers)
    total = 0.0
    for number in numbers:
        total += (number - average) ** 2

    return total / (len(numbers) - 1)

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    return math.sqrt(calculate_variance(numbers))

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_numbers = sorted(number)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    middle1 = sorted_numbers[n // 2 - 1]
    middle2 = sorted_numbers[n // 2]
    return float((middle1 + middle2) / 2)

