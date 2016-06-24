class solutions:
    def maxNumber(self, num1, num2, k):
        maxk = []
        num1_pop = []
        num2_pop = []
        if k == 0:
            return ([],[],[])
        def getmax(num):
            maxv_i = ()
            if num:
                maxv_i = (0,num[0])
            for i,v in enumerate(num):
                if v > maxv_i[1]:
                    maxv_i = (i,v)
            return maxv_i
        maxv_i_1 = getmax(num1)
        maxv_i_2 = getmax(num2)
        if not maxv_i_2 or (maxv_i_1 and maxv_i_1[1] >= maxv_i_2[1]):
            if maxv_i_1[0] == 0:
                num1_pop = []
                num1.pop(0)
            else:
                num1_pop = num1[:maxv_i_1[0]]
                for i in range(maxv_i_1[0]+1):
                    num1.pop(0)
            maxk.append((1, maxv_i_1[0], maxv_i_1[1]))
        else:
            if maxv_i_2[0] == 0:
                num2_pop = []
                num2.pop(0)
            else:
                num2_pop = num2[:maxv_i_2[0]]
                for i in range(maxv_i_2[0]+1):
                    # print(num2)
                    # print(i)
                    num2.pop(0)
            maxk.append((2, maxv_i_2[0], maxv_i_2[1]))
        (n_max, n_num1_pop, n_num2_pop) = self.maxNumber(num1, num2, k-1)
        return (maxk + n_max, num1_pop + n_num1_pop, num2_pop + n_num2_pop)

if __name__ == "__main__":
    num1 = [3, 4, 6, 5]
    num2 = [9, 1, 2, 5, 8, 3]
    test = solutions()
    maxnum = test.maxNumber(num1, num2, 5)
    print(maxnum)
    num1 = [6, 7]
    num2 = [6, 0, 4]
    maxnum = test.maxNumber(num1, num2, 3)
    print(maxnum)
