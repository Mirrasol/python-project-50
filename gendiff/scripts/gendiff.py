#!/usr/bin/env python3

from gendiff.cli import parse_arguments
from gendiff import generate_diff


def main():
    result = parse_arguments()
    file1 = result.first_file
    file2 = result.second_file
    formatter = result.format
    print(generate_diff(file1, file2, formatter))


if __name__ == '__main__':
    main()
