class Solution(object):
    def generateParentheses(self, n):
        re_l = []
        def add_item(l, r, string, res):
            # print(l,r,string,res)
            if l==0 and r ==0:
                res.append(string)
            if l > 0 :
                add_item(l-1, r, string+"(",res)
            if r > 0 and r - l > 0:
                add_item(l, r-1, string+")",res)
        add_item(n, n, "", re_l)
        return re_l

if __name__ == "__main__":
    test = Solution()
    print(test.generateParentheses(1))
    print(test.generateParentheses(2))
    print(test.generateParentheses(3))
    print(test.generateParentheses(4))






