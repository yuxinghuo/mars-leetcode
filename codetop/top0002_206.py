# Definition for singly-linked list.
from typing import List


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]