def reverse_num(num):
    num_remaining, result = num, 0
    while num_remaining:
        result = (result * 10) + (num_remaining % 10)
        num_remaining //= 10

    return result == num


if __name__ == '__main__':
    n = 123321
    rev = reverse_num(n)

    print(f"{n} is palindrome") if rev else print(f"{n} is not palindrome")
        