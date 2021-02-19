from tools import print_exce_time


class Search(object):
    # 二分查找， 非递归
    @staticmethod
    @print_exce_time
    def binary_search(l_s, target):
        n = len(l_s)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right)//2
            if target < l_s[mid]:
                right = mid - 1
            elif target > l_s[mid]:
                left = mid + 1
            else:
                return mid
        return None

    # 二分查找， 递归
    @staticmethod
    @print_exce_time
    def binary_search_rec(nums, target):
        n = len(nums)
        if n < 1:
            return None
        mid = n//2
        if target < nums[mid]:
            return Search.binary_search_rec(nums[:mid], target)
        elif target > nums[mid]:
            return Search.binary_search_rec(nums[mid+1:], target)
        else:
            return mid


if __name__ == '__main__':
    list_example = [64, 34, 25, 12, 22, 11, 90]
    list_example.sort()
    target_example = 34
    ret = Search.binary_search_rec(list_example, target_example)
    print(ret)