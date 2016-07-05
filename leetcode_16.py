class Solution(object):
    def threeSumCloset(self, nums, target):
        nums.sort()
        result_list = []
        result_target = float("-inf")
        print(nums)
        for i in range(len(nums) -2):
            num = nums.pop()
            print(nums)
            two_target =  target - num
            length = len(nums)
            left = 0
            right = length -1
            while left < right:
                added = nums[left] + nums[right]
                if added == two_target:
                    result_list = [num, nums[left], nums[right]]
                    result_target = target
                    return result_target
                elif added < two_target:
                    print("Smaller")
                    print("two_target is {}, added is {}, current result is {}".format(two_target, added, result_target))
                    if abs(two_target - added) < abs(two_target - result_target + num):
                        result_list = [num, nums[left], nums[right]]
                        result_target = num + added
                        print(result_list, result_target)
                    left +=1
                else:
                    print("Bigger")
                    print("two_target is {}, added is {}, current result is {}".format(two_target, added, result_target))
                    if abs(two_target - added) < abs(two_target - result_target + num):
                        result_list = [num, nums[left], nums[right]]
                        result_target = num + added
                        print(result_list, result_target)
                    right -=1
        print(result_list)
        return result_target

if __name__ == "__main__":
    s = [-1, 2, 1, -4]
    target = 1
    test = Solution()
    print(test.threeSumCloset(s, target))
