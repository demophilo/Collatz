#!/usr/bin/env python
# coding: utf-8

# In[19]:


from PIL import Image
import os, sys
from pathlib import Path
from os.path import dirname
import pickle


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
    pickle.dump(target, f)
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
                        current_objects_input.append(pickle.load(openfile))
                    except EOFError:
                        break
            if isinstance(current_objects_input, list) and len(current_objects_input) > 0:
                current_objects = current_objects_input[0]
    return current_objects

def get_next_collatz_number(_num) -> str:
    _trailing_zeros = len(_num) - len(_num.rstrip("0"))
    _next_collatz_number = str(bin(3 * int("0b"+_num, 2) + 2 ** _trailing_zeros))[2:]
    return _next_collatz_number


def collatz_sequence_investigation(_num):
    _line = 1
    while _num.count("1") != 1:
        _num = get_next_collatz_number(_num)
        _line = _line + 1

    _length = len(_num)
    return _line, _length

def collatz_picture(_num, _additional_steps=0):
    _name = _num
    _height, _width = collatz_sequence_investigation(_num)
    _picture_height = _height + _additional_steps
    _picture_width = _width + 2 * _additional_steps
    _pixi = Image.new("1", (_picture_width, _picture_height), "white")
    for _i in range(_picture_height):
        if _i != 0:
            _num = get_next_collatz_number(_num)

        _total_line = "0" * (_picture_width - len(_num)) + _num

        for _k in range(_picture_width):
            _pixi.putpixel((_k, _i), 1 * (_total_line[_k] != "1"))

    _pixi.save(f"Collatz{_name}.bmp")


if __name__ == '__main__':
    skip = 1

    if skip == 0:

        begin_of_sequences = int(input("Beginning:"))
        end_of_sequences = int(input("Ending:")) + 1
        path_cache = "local_cache_4.pck"
        sequence_of_max_every_digit = read_unique_dict(path_cache)

        for length in range(begin_of_sequences, end_of_sequences):
            if length in sequence_of_max_every_digit:
                print(f"Length {length} already calculated and its result is {sequence_of_max_every_digit.get(length)}")
                continue
            print(f"Length {length} to be calculated")
            steps_equal_length = {}
            for j in range(2 ** (length - 2)):
                num = 2 ** (length - 1) + 2 * j + 1
                num = str(bin(num))[2:]
                steps_equal_length[num] = (collatz_sequence_investigation(num)[0])

            maximum_this_digit = max(steps_equal_length.values())
            _counter_max_each_digit = 1

            for _key, _value in steps_equal_length.items():
                if _value == maximum_this_digit:
                    print(length, int("0b" + _key, 2), _key, _value)
                    sequence_of_max_every_digit[length] = {"max-length": maximum_this_digit, "number": _key, "2nd_max": _counter_max_each_digit}
                    _counter_max_each_digit = _counter_max_each_digit + 1

        print(sequence_of_max_every_digit)
        # exit()
        write_to_pickle(sequence_of_max_every_digit, path_cache)
    else:
        print(get_next_collatz_number("101"))







