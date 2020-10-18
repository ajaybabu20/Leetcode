from solutions.PalindromeNumber import Solution


def test_numberone():
    x = 121
    expected = True
    result = Solution().ispalindrome(x)
    assert result == expected


def test_numbertwo():
    x = -101
    expected = False
    result = Solution().ispalindrome(x)
    assert result == expected


def test_numberthree():
    x = -121
    expected = False
    result = Solution().ispalindrome(x)
    assert result == expected


def test_numberfour():
    x = 10
    expected = False
    result = Solution().ispalindrome(x)
    assert result == expected
