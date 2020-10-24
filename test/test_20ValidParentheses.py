from solutions.ValidParentheses import Solution


def test_numberone():
    s = "()"
    expected = True
    result = Solution().isValid(s=s)
    assert result == expected


def test_numbertwo():
    s = "()[]{}"
    expected = True
    result = Solution().isValid(s=s)
    assert result == expected


def test_numberthree():
    s = "(]"
    expected = False
    result = Solution().isValid(s=s)
    assert result == expected


def test_numberfour():
    s = "([)]"
    expected = False
    result = Solution().isValid(s=s)
    assert result == expected


def test_numberfive():
    s = "{[]}"
    expected = True
    result = Solution().isValid(s=s)
    assert result == expected


def test_numbersix():
    s = "["
    expected = False
    result = Solution().isValid(s=s)
    assert result == expected


def test_numberseven():
    s = "(("
    expected = False
    result = Solution().isValid(s=s)
    assert result == expected
