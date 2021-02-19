from tools import print_exce_time


class Stack(object):

    # 括号配对
    @staticmethod
    @print_exce_time
    def kh_match(s):
        dict_kh = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for item in s:
            if item in '([{':
                stack.append(item)
            elif item in ')]}':
                if not stack:
                    return False
                if dict_kh.get(item) == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
