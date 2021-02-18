from common import print_exce_time


class Sort(object):
    def __init__(self, list_old):
        self.list_old = list_old

    # 冒泡排序
    @print_exce_time
    def bubble_sort(self):
        n = len(self.list_old)
        for i in range(n):
            for j in range(n-i-1):
                if self.list_old[j] > self.list_old[j+1]:
                    self.list_old[j], self.list_old[j+1] = self.list_old[j+1], self.list_old[j]


if __name__ == '__main__':
    list_source = [64, 34, 25, 12, 22, 11, 90]
    print('old list is {}'.format(list_source))
    Sort(list_source).bubble_sort()
    print('new list is: {}'.format(list_source))
