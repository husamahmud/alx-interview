#!/usr/bin/python3
"""Defines a function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    res = [[1]]

    for i in range(n - 1):
        li = [1]
        for j in range(i):
            li.append(res[i][j] + res[i][j + 1])
        li.append(1)
        res.append(li)

    return res
