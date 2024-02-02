#!/usr/bin/env python3

from gendiff.parser import parse
from gendiff.gendiff import generate_diff


def main():
    result = parse()
    file1 = result.first_file
    file2 = result.second_file
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
