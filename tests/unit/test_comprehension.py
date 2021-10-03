from python_examples.comprehension import (
    get_numbers_and_square,
    get_odd_numbers,
    get_unique_numbers,
    main,
)


def test_get_odd_numbers():
    assert get_odd_numbers([]) == []
    assert get_odd_numbers([1]) == [1]
    assert get_odd_numbers([1, 2, 3]) == [1, 3]
    assert get_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]


def test_get_numbers_and_square():
    assert get_numbers_and_square([]) == {}
    assert get_numbers_and_square([1]) == {1: 1}
    assert get_numbers_and_square([1, 2, 3]) == {1: 1, 2: 4, 3: 9}
    assert get_numbers_and_square([1, 2, 3, 4, 5]) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def test_get_unique_numbers():
    assert get_unique_numbers([]) == set()
    assert get_unique_numbers([1]) == {1}
    assert get_unique_numbers([1, 1, 1]) == {1}
    assert get_unique_numbers([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == {1, 2, 3, 4, 5}


def test_main():
    main()
