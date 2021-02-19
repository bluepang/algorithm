from tools import print_exce_time


class DP(object):

    # 爬楼梯，计算n阶楼梯，有多少种爬的路径
    @staticmethod
    @print_exce_time
    def climb_stairs(n):
        if n == 0:
            print('请输入正整数')
            return None
        p, q = 0, 1
        # print(p)
        # print(q)
        for i in range(n):
            r = p + q
            p = q
            q = r
            # print(r)
        return r

    # 斐波拉契数列
    @staticmethod
    @print_exce_time
    def fibo(n):
        fibos = []
        if n == 0:
            print('请输入一个正整数')
        elif n == 1:
            fibos.append(0)
        else:
            p, q = 0, 1
            for i in range(n):
                if i < 2:
                    fibos.append(i)
                else:
                    r = p + q
                    p = q
                    q = r
                    fibos.append(r)
        return fibos


if __name__ == '__main__':
    ret = DP.climb_stairs(4)
    print(ret)