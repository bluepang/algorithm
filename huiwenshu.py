from tools import print_exce_time


class HWS(object):

    # 回文数，字符串切片
    @staticmethod
    @print_exce_time
    def hws_str_cut(n):
        return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = 1234
    ret = HWS.hws_str_cut(n)
    print(ret)
