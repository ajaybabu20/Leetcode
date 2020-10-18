from solutions.TwoSum import Solution


def test_numberone():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = Solution().twosum(nums=nums, target=target)
    assert expected == result

def test_numbertwo():
    nums = [3, 2, 4]
    target = 6
    expected = [1,2]
    result = Solution().twosum(nums=nums, target=target)
    assert expected == result

def test_numberthree():
    nums = [3, 3]
    target = 6
    expected = [0,1]
    result = Solution().twosum(nums=nums, target=target)
    assert expected == result

def test_numberfour():
    nums = [3, 2, 3]
    target = 6
    expected = [0,2]
    result = Solution().twosum(nums=nums, target=target)
    assert expected == result