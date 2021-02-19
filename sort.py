from tools import print_exce_time


class Sort(object):

    # 冒泡排序
    @staticmethod
    @print_exce_time
    def bubble_sort(nums):
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    # 快速排序
    @staticmethod
    @print_exce_time
    def quick_sort(nums):
        n = len(nums)
        if n < 2:
            return nums
        else:
            pivot = nums[0]
            low = [item for item in nums if item < pivot]
            high = [item for item in nums if item > pivot]
            return Sort.quick_sort(low) + [pivot] + Sort.quick_sort(high)

    # 选择排序
    @staticmethod
    @print_exce_time
    def select_sort(nums):
        new_list = []

        def find_min_index(nums_inner):
            min_index_inner = 0
            n = len(nums_inner)
            for i in range(n):
                if nums_inner[i] < nums_inner[min_index_inner]:
                    min_index_inner = i
            return min_index_inner

        for i in range(len(nums)):
            min_index = find_min_index(nums)
            min_item = nums.pop(min_index)
            new_list.append(min_item)

        return new_list

    # 插入排序
    @staticmethod
    @print_exce_time
    def insert_sort(nums):
        n = len(nums)
        for i in range(1, n):
            value = nums[i]
            j = i - 1
            while j >= 0:
                if nums[j] > value:
                    nums[j+1] = nums[j]
                else:
                    break
                j -= 1
            nums[j+1] = value
        return nums


if __name__ == '__main__':
    list1 = [64, 34, 25, 12, 22, 11, 90]
    print('old list is {}'.format(list1))
    print('new list is: {}'.format(Sort.insert_sort(list1)))
