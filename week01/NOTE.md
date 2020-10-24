# 学习笔记

**刷题遍数很重要，刷题遍数很重要，刷题遍数很重要**

## Array List
- Double pointer
- Sliding Window -> Queue
- 夹逼

## Linked List
- 多练
- LRU cache [LC146](https://leetcode.com/problems/lru-cache/)

## Skip List
- Basics
  - Must be sorted
  - Update each level of index
- Redis impelementation

## Stack
- FILO
- Find left and right bounds
- DFS

## Queue
- FIFO
- BFS
- Sliding Window

## Deque
- `from collections import deque`

## Priority Queue
```python
import heapq

heap = []
heapq.heapify(heap)
heapq.heappush(heap, a)
# heap is sorted by each element of a
# To store an object as a, make it a set like (prio, a), so that heap will be sorted by prio.
# There is no maxheap in python, use (-prio), instead.
b = heapq.heappop(heap)
```