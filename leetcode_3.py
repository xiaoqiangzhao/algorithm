class Solution(object):
    def lengthOfLongestSubstring_1(self, s):
        length = len(s)
        locator = 0
        start_max = 0
        end_max = 0
        start = 0
        end = 0
        while locator <  length:
            # print(s[locator], s[start : locator])
            end = locator - 1
            if s[locator] in s[start : locator]:
                if end - start > end_max - start_max :
                    start_max = start
                    end_max = end
                start = locator
            locator += 1
        if length - 1 - start > end_max - start_max and end < start - 1:
            start_max , end_max = (start, length -1)
        return (s[start_max : end_max + 1] , end_max , start_max )

    def lengthOfLongestSubstring_2(self, s):
        list_s = []
        def sub_string(s):
            length = len(s)
            for i in range(length):
                if s[i] in s[:i]:
                    list_s.append(s[:i])
                    sub_string(s[i:])
                    break
                if i == length -1:
                    list_s.append(s)
        sub_string(s)
        s_result = list_s[0]
        s_length = len(s_result)
        for s_i in list_s[1:]:
            if len(s_i) > s_length:
                s_result = s_i
        return(s_result, len(s_result))



if __name__ == "__main__":
    test = Solution()
    s = "abcabcbb"
    print(test.lengthOfLongestSubstring_1(s))
    print(test.lengthOfLongestSubstring_2(s))
    s = "bbbb"
    print(test.lengthOfLongestSubstring_1(s))
    print(test.lengthOfLongestSubstring_2(s))
    s = "pwwkew"
    print(test.lengthOfLongestSubstring_1(s))
    print(test.lengthOfLongestSubstring_2(s))


