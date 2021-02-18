from tools import print_exce_time


class Sort(object):

    # 冒泡排序
    @staticmethod
    @print_exce_time
    def bubble_sort(list_old):
        n = len(list_old)
        for i in range(n):
            for j in range(n-i-1):
                if list_old[j] > list_old[j+1]:
                    list_old[j], list_old[j+1] = list_old[j+1], list_old[j]
        return list_old

    # 快速排序
    @staticmethod
    @print_exce_time
    def quick_sort(list_old):
        n = len(list_old)
        if n < 2:
            return list_old
        else:
            pivot = list_old[0]
            low = [item for item in list_old if item < pivot]
            high = [item for item in list_old if item > pivot]
            return Sort.quick_sort(low) + [pivot] + Sort.quick_sort(high)


if __name__ == '__main__':
    list_source = [64, 34, 25, 12, 22, 11, 90]
    print('old list is {}'.format(list_source))
    print('new list is: {}'.format(Sort.quick_sort(list_source)))
