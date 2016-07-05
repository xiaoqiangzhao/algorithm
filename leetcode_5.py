class Solution(object):
    def longestPalindrome(self, s):
        l_s = list(s)
        l_r_s = list(reversed(s))
        header = 0
        length =len(s)
        start = 0
        end = 1
        while header < length:
            for i in range(header,length):
                if not l_s[i] == l_r_s[i]:
                    if i - header > end - start:
                        start = header
                        end = i
                    header = i + 1
                    break
        return s[start:end]

if __name__ == "__main__":
    test = Solution()
    s = "abcdabbadcafmnbvcvbnm"
    print(test.longestPalindrome(s))

