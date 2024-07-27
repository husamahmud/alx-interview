#!/usr/bin/env python3
"""Lockboxes"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
	"""
	Check if all lockboxes are unlocked
	"""
	n = len(boxes)
	visited = set()
	stack = [0]
	while stack:
		curr = stack.pop()
		if curr not in visited:
			visited.add(curr)

			for key in boxes[curr]:
				if 0 <= key < n and key not in visited:
					stack.append(key)

	return len(visited) == n
