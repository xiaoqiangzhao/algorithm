class Solution(object):
    def threeSum(self, nums):
        results = []
        def twoSum(sorted_nums, target):
            results = []
            length = len(nums)
            left = 0
            right = length -1
            while left < right:
                added = sorted_nums[left] + sorted_nums[right]
                if added == target:
                    results.append([sorted_nums[left], sorted_nums[right]])
                    right -=1
                    left +=1
                elif added < target:
                    left +=1
                else:
                    right -=1
            return results



            # for i in range(lengh)1:
                # if i == lengh -1:
                    # break
                # for j in range(i + 1, lengh):
                    # if nums[i] + nums[j] == target:
                        # results.append([nums[i], nums[j]])
            return results
        nums.sort()
        for i in range(len(nums) -2):
            num = nums.pop()
            target =  -num
            results2add = twoSum(nums, target)
            if results2add:
                for result in results2add:
                    if [num] + result in results:
                        continue
                    results.append([num] + result)
        return results
        # def twoSum(nums, target):
            # for i in range(len(nums)):
                # if i == len(nums) -1:
                    # break
                # for j in range(i + 1, len(nums)):
                    # if nums[i] + nums[j] == target:
                        # yield [nums[i], nums[j]]
        # for i in range(len(nums) -2):
            # num = nums.pop(0)
            # print(num)
            # print(nums)
            # target =  -num
            # for result in twoSum(nums, target):
                # result_add = [num] + result
                # result_add.sort()
                # if result_add in results:
                    # continue
                # results.append(result_add)
        # return results

if __name__ == "__main__":
    test = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    results = test.threeSum(nums)
    print(results)




