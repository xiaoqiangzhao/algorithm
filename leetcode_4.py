class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        length1 = len(num1)
        length2 = len(num2)
        def getmedian(nums):
            length = len(nums)
            print(nums)
            if length % 2:
                return nums[length//2]
            else:
                return (nums[length//2] + nums[length//2 - 1])/2
        if length1 == length2:
            if num1[-1] <= num2[0]:
                return (num1[-1] + num2[0]) /2
            elif num2[-1] <= num1[0]:
                return (num1[0] + num2[-1]) /2
            else:
                i = 0
                while i != length1 - 1:
                    m_1 = getmedian(num1[i:])
                    m_2 = getmedian(num2[i:])
                    if m_1 == m_2:
                        return m_1
                    i = (i + length1)//2
if __name__ == "__main__":
    test = Solution()
    num1 = [1, 2, 3]
    num2 = [1, 1, 4]
    median = test.findMedianSortedArrays(num1, num2)
    print(median)

