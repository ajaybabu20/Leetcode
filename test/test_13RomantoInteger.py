from solutions.RomantoInteger import Solution


def test_numberone():
    val = "III"
    expected = 3
    result = Solution().romantoint(val)
    assert expected == result


def test_numbertwo():
    val = "IV"
    expected = 4
    result = Solution().romantoint(val)
    assert expected == result


def test_numberthree():
    val = "IX"
    expected = 9
    result = Solution().romantoint(val)
    assert expected == result


def test_numberfour():
    val = "LVIII"
    expected = 58
    result = Solution().romantoint(val)
    assert expected == result


def test_numberfive():
    val = "MCMXCIV"
    expected = 1994
    result = Solution().romantoint(val)
    assert expected == result


def test_numbersix():
    val = "MCDLXXVI"
    expected = 1476
    result = Solution().romantoint(val)
    assert expected == result
