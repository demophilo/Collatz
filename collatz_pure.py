#!/usr/bin/env python
# coding: utf-8
import os
import pickle as pkl
import time
from os.path import dirname
from pathlib import Path
from PIL import Image
import numpy as np


def write_to_pickle(target, target_path):
    """
    :param target:
    :param target_path:
    :return:
    """
    if not isinstance(target_path, str):
        target_path = str(target_path)
    Path(dirname(target_path)).mkdir(parents=True, exist_ok=True)
    f = open(target_path, 'wb')
    pkl.dump(target, f)
    f.close()


def read_unique_dict(path):
    """
    :param skip:
    :param path:
    :return:
    """
    current_objects = dict()
    if True:
        if os.path.exists(path):
            current_objects_input = []
            with (open(path, "rb")) as openfile:
                while True:
                    try:
                        current_objects_input.append(pkl.load(openfile))
                    except EOFError:
                        break
            if isinstance(current_objects_input, list) and len(current_objects_input) > 0:
                current_objects = current_objects_input[0]
    return current_objects


def get_power_of_two(_num):
    _power_of_2 = 0
    while (_num % 2 == 0):
        _num = _num >> 1
        _power_of_2 = _power_of_2 + 1

    return _power_of_2


def get_next_collatz_number(_num) -> int:
    _power_of_two = get_power_of_two(_num)
    _next_collatz_number = ((_num >> _power_of_two) * 3 + 1) << _power_of_two
    return _next_collatz_number


def get_collatz_length(_num):
    if _num == 0:
        return 0
    _striped_num = _num >> get_power_of_two(_num)
    _collatz_length = 1
    while _striped_num >> 1 != 0:
        _striped_num = _striped_num >> 1
        _collatz_length = _collatz_length + 1

    return _collatz_length


def collatz_sequence_investigation(_num):
    _line = 1
    while get_collatz_length(_num) != 1:
        _num = get_next_collatz_number(_num)
        _line = _line + 1

    _length = get_power_of_two(_num) + 1

    return np.array([_line, _length])


def convert_number_to_binary_string(_num):
    return str(bin(_num))[2:]


def convert_binary_string_to_number(_binary_string):
    return int("0b" + _binary_string, base=2)


def create_picture_of_collatz_sequence(_num, _additional_steps=0):
    _filename = convert_number_to_binary_string(_num)
    _height, _width = collatz_sequence_investigation(_num)
    _picture_height = _height + _additional_steps
    _picture_width = _width + 2 * _additional_steps
    _picture_of_collatz_sequence = Image.new("1", (_picture_width, _picture_height), "white")
    _collatz_number = _num
    for _row in range(_picture_height):
        if _row != 0:  # first row is the number itself
            _collatz_number = get_next_collatz_number(_collatz_number)

        _binary_num_string = convert_number_to_binary_string(_collatz_number)

        _total_line = "0" * (_picture_width - len(_binary_num_string)) + _binary_num_string

        for _column in range(_picture_width):
            _picture_of_collatz_sequence.putpixel((_column, _row), 1 * (_total_line[_column] != "1"))

    _picture_of_collatz_sequence.save(f"Collatz{_filename}.bmp")


def make_dict_of_max_collatz_steps_per_digit(begin_of_sequences, end_of_sequences):
    path_cache = "local_cache_4.pck"
    sequence_of_max_every_digit = read_unique_dict(path_cache)

    for length in range(begin_of_sequences, end_of_sequences + 1):
        if length in sequence_of_max_every_digit:
            print(f"Length {length} already calculated and its result is {sequence_of_max_every_digit.get(length)}")
            continue
        print(f"Length {length} to be calculated")
        steps_equal_length = {}
        for j in range(1 << (length - 2)):
            _num = 1 << (length - 1) + j << 1 + 1
            steps_equal_length[_num] = (collatz_sequence_investigation(_num)[0])

        maximum_this_digit = max(steps_equal_length.values())
        _counter_max_each_digit = 1

        for _key, _value in steps_equal_length.items():
            if _value == maximum_this_digit:
                print(length, int("0b" + _key, 2), _key, _value)
                sequence_of_max_every_digit[length] = {"max-length": maximum_this_digit, "number": _key,
                                                       "2nd_max": _counter_max_each_digit}
                _counter_max_each_digit = _counter_max_each_digit + 1

    print(sequence_of_max_every_digit)
    write_to_pickle(sequence_of_max_every_digit, path_cache)





if __name__ == '__main__':

    print(collatz_sequence_investigation(3))

    length = 6
    numbers_with_given_collatz_length = (((1 << (length - 1)) + 1) + 2 * i for i in range(0, 1 << (length - 2)))
    for number in numbers_with_given_collatz_length:
        print(number, collatz_sequence_investigation(number))