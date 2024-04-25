#!/usr/bin/python3
"""Defines a function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    row = [1]
    res = pascal_triangle(n - 1)
    last_row = res[-1]

    for i in range(len(last_row) - 1):
        row.append(last_row[i] + last_row[i + 1])

    row += [1]
    res.append(row)
    return res
