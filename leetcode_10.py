class Solution(object):
    def isMatch(self, s, p):
        # print(s,p,sep="=>")
        flag = False
        length_s = len(s)
        length_p = len(p)
        i = length_s - 1
        def Ignorable(p):
            length = len(p)
            if length % 2:
                return False
            else:
                for i in range(length):
                    if i % 2:
                        if not  p[i] == "*":
                            return False
                    else:
                        if not ((p[i] > 'A' and p[i] <= 'z') or p[i] == "."):
                            return False
                else:
                    return True

        def single_char_match(char, p):
            length = len(p)
            if length == 0:
                return False
            if length <=2 :
                if p in [".", ".*", char, char+"*"]:
                    return True
                else:
                    return False
            else:
                if p[-2:] in [".*", char+"*", ]:
                    if single_char_match(char, p[:-2]) or Ignorable(p[:-2]):
                        return True
                    else:
                        return False
                elif p[-1] in [char, "."]:
                    if Ignorable(p[:-1]):
                        return True
                    else:
                        return False
                elif Ignorable(p[-2:]):
                    return single_char_match(char, p[:-2])
                else:
                    return False

        if length_p == 0 and not length_s == 0:
            return False
        if length_s == 0:
            if Ignorable(p):
                return True
            else:
                return False
        char = s[i]
        if length_s == 1:  ## wait for fix
            return single_char_match(char, p)
        else:
            if p[-1] == '.':
                if self.isMatch(s[:i], p[:length_p - 1]):
                    return True
                else:
                    return False
            elif p[-1] == '*':
                if not p[-2] in [char, '.']:
                    if self.isMatch(s, p[:length_p -2]):
                        return True
                    else:
                        return False
                else:
                    if self.isMatch(s[:i], p) or self.isMatch(s[:i], p[:length_p - 2]) or self.isMatch(s,p[:length_p -2]):
                        return True
                    else:
                        return False
            else:  ##[a-ZA-Z]
                if not char == p[-1]:
                    return False
                else:
                    if self.isMatch(s[:i], p[:length_p - 1]):
                        return True
                    else:
                        return False

if __name__ == "__main__":
    test = Solution()
    print(test.isMatch("aa", "a"))
    print(test.isMatch("aa", "aa"))
    print(test.isMatch("aaa", "aa"))
    print(test.isMatch("aa", "a*"))
    print(test.isMatch("aa", ".*"))
    print(test.isMatch("ab", ".*"))
    print(test.isMatch("aab", "c*a*b*"))
    print(test.isMatch("abcd", "d*"))
    print(test.isMatch("", ".*"))
    print(test.isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"))
    print(test.isMatch("aasdfasdfasdf", "aasdf.*asdf.*asdf.*"))


