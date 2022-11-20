#!/usr/bin/env python3

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()


def parse_input(input):
    """
    Get a input as a string
    Return a list of strings
    """
    return input[1:-1].replace('"', '').replace(' ', '').replace('\n', '').split(',')


def remove_repeated_beginning(list_of_elements):
    """
    Precondition: list_of_elements is a non-empty list of elements and not all elements are the same.
    Given a list of elements, remove the repeated beginning of the list.
    Examples:
    [A,A,A,B,C,D] -> [A,B,C,D]
    [A,B,C,D] -> [A,B,C,D]
    [C,C,C,C,A,B,C,D] -> [C,A,B,C,D]
    """
    if (len(list_of_elements) == 1):
        return list_of_elements

    i = 0
    # find the first element that is not equal to the first element
    while (list_of_elements[i] == list_of_elements[0]):
        i += 1
    return list_of_elements[i-1:]


def get_zebra_pattern(list_of_elements):
    if len(list_of_elements) == 1:
        return list_of_elements[0], 1
    if len(set(list_of_elements)) == 1:
        return list_of_elements[0], 1
    list_of_elements = remove_repeated_beginning(list_of_elements)
    longest_zebra = [list_of_elements[0], list_of_elements[1]]
    zebra_size = 2
    current_zebra = [list_of_elements[0], list_of_elements[1]]
    current_zebra_size = 2
    for i in range(2, len(list_of_elements)):
        # if next element is equal to the first element of the current zebra pattern
        if list_of_elements[i] == current_zebra[0]:
            current_zebra = [current_zebra[1], list_of_elements[i]]
            current_zebra_size += 1
            # if current zebra pattern is longer than the longest zebra pattern
            if current_zebra_size > zebra_size:
                zebra_size = current_zebra_size
                longest_zebra = current_zebra
        elif i + 1 == len(list_of_elements):
            if zebra_size == 2:
                return list_of_elements[-1], 2
        else:
            current_zebra = [current_zebra[1], list_of_elements[i]]
            current_zebra_size = 2
    return longest_zebra[1], zebra_size


def main():
    input = read_file("colors.txt")
    parsed_input = parse_input(input)
    last_pattern_element, pattern_size = get_zebra_pattern(parsed_input)
    print(f"submit {pattern_size}@{last_pattern_element}")


if __name__ == "__main__":
    main()
