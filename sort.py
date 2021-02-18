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

    # 选择排序
    @staticmethod
    @print_exce_time
    def select_sort(list_old):
        new_list = []

        def find_min_index(list_source):
            min_index_inner = 0
            n = len(list_source)
            for i in range(n):
                if list_source[i] < list_source[min_index_inner]:
                    min_index_inner = i
            return min_index_inner

        for i in range(len(list_old)):
            min_index = find_min_index(list_old)
            min_item = list_old.pop(min_index)
            new_list.append(min_item)

        return new_list

    # 插入排序
    @staticmethod
    @print_exce_time
    def insert_sort(list_old):
        n = len(list_old)
        for i in range(1, n):
            value = list_old[i]
            j = i - 1
            while j >= 0:
                if list_old[j] > value:
                    list_old[j+1] = list_old[j]
                else:
                    break
                j -= 1
            list_old[j+1] = value
        return list_old


if __name__ == '__main__':
    list1 = [64, 34, 25, 12, 22, 11, 90]
    print('old list is {}'.format(list1))
    print('new list is: {}'.format(Sort.insert_sort(list1)))
