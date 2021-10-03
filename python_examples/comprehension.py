"""Comprehension module."""

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_odd_numbers(num_list: list) -> list:
    """Returns a list of odd numbers from a list."""
    return [num for num in num_list if num % 2 != 0]


def get_numbers_and_square(num_list: list) -> dict:
    """Returns a dict with number and number^2 from a list."""
    return {num: num * num for num in num_list}


def get_unique_numbers(num_list: list) -> set:
    """Returns unique values from a list."""
    return {num for num in num_list}


def main() -> None:
    """Main func."""
    print(f"{get_odd_numbers(L)=}")
    print(f"{get_numbers_and_square(L)=}")
    print(f"{get_unique_numbers(L)=}")


if __name__ == "__main__":
    main()
