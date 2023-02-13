def perfect_number(number:int):
    answer = False
    proper_divisors = []
    for i in range(1, number):
        if number%i == 0:
            proper_divisors.append(i)
    if sum(proper_divisors) == number:
        answer = True
    return answer

def main():
    for i in range(1,100001):
        val = perfect_number(j)
        if val is True:
            print(j)
main()