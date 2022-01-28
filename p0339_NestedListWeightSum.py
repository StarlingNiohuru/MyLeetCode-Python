from collections import deque
from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


# BFS
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth, res = 1, 0
        q = deque(nestedList)
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.isInteger():
                    res += depth * curr.getInteger()
                else:
                    q.extend(curr.getList())
            depth += 1
        return res
