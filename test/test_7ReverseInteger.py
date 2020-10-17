from solutions.ReverseInteger import Solution


def test_numberone():
    value = 123
    expected = 321
    result = Solution().reverse(value)
    assert result == expected


def test_numbertwo():
    value = -123
    expected = -321
    result = Solution().reverse(value)
    assert result == expected


def test_numberthree():
    value = 120
    expected = 21
    result = Solution().reverse(value)
    assert result == expected


def test_numberfour():
    value = 0
    expected = 0
    result = Solution().reverse(value)
    assert result == expected


def test_numberfive():
    value = 1534236469
    expected = 0
    result = Solution().reverse(value)
    assert result == expected
