class Solution(object):

    def longestcommonprefix(self, strs):
        com_str = ""
        if not strs:
            return com_str
        length = min([len(s) for s in strs])
        for i in range(length):
            for s in strs[1:]:
                if not strs[0][:i+1] == s[:i+1]:
                    return com_str
            else:
                com_str = strs[0][:i+1]
        return com_str

if __name__ == "__main__":
    s_a = "abcde"
    s_b = "abcdeh"
    s_c = "abcdegi"
    s_d = "abcdefgi"
    strs = [s_a, s_b, s_c, s_d]
    test = Solution()
    print(test.longestcommonprefix(strs))
