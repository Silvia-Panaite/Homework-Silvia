n = int(input('Please type in an integer number: '))

def proper_divisor(n: int) -> list:
    list_ = []
    for i in range(1, (n//2) + 1):
        if n % i == 0:
            list_.append(i)
    return list_

print(proper_divisor(n))

def main():
    n = int(input('Please enter a positive integer: '))
    print('The list of proper divisors of', n, 'is:')
    print(proper_divisor(n))
    


