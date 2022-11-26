def ndigits(number):
    return len(str(number))


def nth_digit(number, n):
    return int(str(number)[n])


def nth_lte_next_digit(number, n):
    return nth_digit(number, n) <= nth_digit(number, n + 1)


def check(number):
    # Clue 1
    len_digits = ndigits(number)
    if len_digits != 5:
        return False

    # Clue 2
    # number has the number 5 repeated at least twice
    if str(number).count("5") < 2:
        return False

    # Clue 3
    for i in range(len_digits - 1):
        if not nth_lte_next_digit(number, i):
            return False

    return True


def get_password_candidates():
    """
    Get password.
    Clues:
    1. The password is 5-digit number.
    2. The password has the number 5 repeated twice.
    3. Every digit is less or equal than the next digit.
    4. The password a number greater than 11098 and 98123.
    For example,
    55678 is a valid password.
    12355 is a valid password.
    12345 is not a valid password.
    57775 is not a valid password.
    Get the number of passwords that fulfill the clues.
    """
    candidates = []
    for i in range(11099, 98123):
        if check(i):
            candidates.append(i)

    return candidates


def main():
    candidates = get_password_candidates()
    print(f"submit {len(candidates)}-{candidates[55]}")


# Default main boilerplate
if __name__ == '__main__':
    main()
