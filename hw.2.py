
import random

def get_numbers_ticket(min, max, quantity):

    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
    return numbers


print(get_numbers_ticket(1, 49, 6))