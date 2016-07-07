class Solution(object):
    def isValid(self, s):
        # print(s)
        start = 0
        end = 0
        length = len(s)
        depth = 1
        if length % 2:
            return False
        def pair_match(left, right):
            if (left, right) in [("(", ")"), ("{", "}"), ("[", "]")]:
                return True
            else:
                return False

        for i in range(1,length):
            # print (depth)
            if i == start:
                continue
            if s[i] == s[start]:
                depth += 1
            if pair_match(s[start], s[i]):
                depth -= 1
                if depth == 0:
                    # print(start, i)
                    if i - start >1 :
                        if self.isValid(s[start + 1: i]):
                            start = i + 1
                            depth = 1
                        else:
                            return False
                    else:
                        start = i + 1
                        depth = 1
        else:
            if not start == length:
                return False
            else:
                return True

if __name__ == "__main__":
    test = Solution()
    string = "()[]{}"
    print(test.isValid(string))

    string = "([)]{}"
    print(test.isValid(string))

    string = "([]){}"
    print(test.isValid(string))
    string = "[({(())}[()])]"
    print(test.isValid(string))

