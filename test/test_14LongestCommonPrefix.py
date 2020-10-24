from solutions.LongestCommonPrefix import Solution


def test_numberone():
    strs = ["flower", "flow", "flight"]
    expected = "fl"
    result = Solution().longestcommonprefix(strs=strs)
    assert expected == result

def test_numbertwo():
    strs = ["dog","racecar","car"]
    expected = ""
    result = Solution().longestcommonprefix(strs=strs)
    assert expected == result

def test_numberthree():
    strs = ["dog","dog","dog"]
    expected = "dog"
    result = Solution().longestcommonprefix(strs=strs)
    assert expected == result
