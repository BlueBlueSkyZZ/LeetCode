from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = []
        for i in range(n):
            nums2.append(nums[i])
            nums2.append(nums[i + n])
        return nums2

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        """
        liuyubobobo思路：
        一个 int 有 32 个 bit，所以我们还可以使用剩下的 22 个 bit 做存储。实际上，每个 int，我们再借 10 个 bit 用就好了。
        因此，在下面的代码中，每一个 nums[i] 的最低的十个 bit（0-9 位），我们用来存储原来 nums[i] 的数字；再往前的十个 bit（10-19 位），我们用来存储重新排列后正确的数字是什么。
        在循环中，我们每次首先计算 nums[i] 对应的重新排列后的索引 j，之后，取 nums[i] 的低 10 位（nums[i] & 1023），即 nums[i] 的原始信息，把他放到 nums[j] 的高十位上。
        最后，每个元素都取高 10 位的信息(e >> 10)，即是答案。
        :param nums:
        :param n:
        :return:
        """
        for i in range(2 * n):
            j = 2 * i if i < n else 2 * (i-n) + 1
            nums[j] |= ((nums[i] & 1023) << 10)
        result = [x >> 10 for x in nums]
        return result



if __name__ == '__main__':
    solution = Solution()
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(solution.shuffle(nums, n))
    print(solution.shuffle2(nums, n ))

