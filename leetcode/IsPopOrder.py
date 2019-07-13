# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not popV and not pushV:
            return True
        if not popV:
            return False
        temp = []
        count = 0
        lens = len(pushV)
        for i in popV:
            if len(temp) == 0 or temp[-1] != i:
                # 防止20行count++后，超出list范围
                if count >= lens:
                    return False
                while pushV[count] != i:
                    temp.append(pushV[count])
                    count += 1
                    if count >= lens:
                        return False
                count += 1
            else:
                temp.pop()
        return True


pushV = [1, 2, 3, 4, 5]
popV = [4, 3, 5, 2, 1]
t = Solution()
a = t.IsPopOrder(pushV, popV)
print(a)
