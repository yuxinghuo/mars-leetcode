class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3))
