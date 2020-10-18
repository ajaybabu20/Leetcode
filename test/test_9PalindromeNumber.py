from solutions.PalindromeNumber import  Solution

def test_numberone():
    x = 121
    expected = True
    result = Solution().isPalindrome(x)
    assert result == expected

def test_numberone():
    x = -101
    expected = False
    result = Solution().isPalindrome(x)
    assert result == expected


def test_numberone():
    x = -121
    expected = False
    result = Solution().isPalindrome(x)
    assert result == expected


def test_numberone():
    x = 10
    expected = False
    result = Solution().isPalindrome(x)
    assert result == expected