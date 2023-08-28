def is_armstrong_number(number):
    digits = str(number)
    return sum([int(n) ** len(digits) for n in digits]) == number
    
