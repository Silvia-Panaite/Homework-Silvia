def proper_divisor(n: int) -> list:
    list_ = []
    for i in range(1, (n//2) + 1):
        if n % i == 0:
            list.append(i)
    return list_

def main():
    n = int(input('Please enter a positiver integer: '))
    print('The list of proper divisors of', n, 'is:')
    print(proper_divisor(n))

if __name__ == '_main_':
    main()
    




