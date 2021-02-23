from tools import print_exce_time


class String(object):

    # 回文数，字符串切片
    @staticmethod
    @print_exce_time
    def hws_str_cut(n):
        return str(n) == str(n)[::-1]

    # 最长不重复子串，没看懂！！！，先记上
    @staticmethod
    @print_exce_time
    def longest_sub_string(s):
        temp_dict = {}
        temp_list = []
        start, max_length = 0, 0
        n = len(s)
        for i in range(n):
            cur = s[i]
            if cur in temp_dict:
                start = max(temp_dict[cur]+1, start)
            elif i-start+1 >= max_length:
                max_length = i-start+1
                temp_list.append(s[start:i+1])
            temp_dict[cur] = i
        ret = ','.join([i for i in temp_list if len(i) == max_length])
        return ret, max_length


if __name__ == '__main__':
    n = 1234
    ret = String.hws_str_cut(n)
    print(ret)
