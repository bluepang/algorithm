from tools import print_exce_time


class Nums(object):

    # 旋转数组
    @staticmethod
    @print_exce_time
    def rotate_nums(nums, k):
        n = len(nums)
        k = k % n
        new_nums = []

        # 切片拼接
        # nums[:] = nums[-k:] + nums[:-k]
        # new_nums = nums

        # 从-k开始，一个个加到新数组
        # for i in range(n):
        #     new_nums.append(nums[i-k])

        # 入队出队
        for _ in range(k):
            ret = nums.pop()
            nums.insert(0, ret)
        new_nums = nums

        return new_nums

    # 双数之和
    @staticmethod
    @print_exce_time
    def sum_two(nums, target):
        n = len(nums)
        ret = []
        start = 0
        end = n - 1
        while start < end:
            if nums[start] + nums[end] == target:
                ret.append()

    # 反转数组
    @staticmethod
    @print_exce_time
    def rev_nums(nums):
        # 解法一：切片
        # return nums[::-1]

        # 解法二：list方法/函数
        # nums.reverse()
        # return nums

        # 解法三：双指针交换
        n, left, right = len(nums), 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    new_nums = Nums.rotate_nums(nums, 13)
    print(new_nums)