class solutions(object):
    def __init__(self):
        pass
    def twosum(self, nums, target):
        print("nums: {}  target: {}".format(nums, target))
        for i in range(len(nums)):
            if i == len(nums) -1:
                break
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    yield (i, j)


if __name__ == "__main__":
    test = solutions()
    num_list = [2, 7, 11, 15, 1, 8, 1]
    target = 9

    for re in test.twosum(num_list, target):
        print(re)

