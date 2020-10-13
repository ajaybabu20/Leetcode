from solutions.SetMismatch import Solution


def test_base():
    nums = [1, 2, 2, 4]
    expected = [2, 3]
    result = Solution().findErrorNums(nums=nums)
    assert result == expected