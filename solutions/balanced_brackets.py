#https://www.hackerrank.com/challenges/ctci-balanced-brackets

def is_matched(expression):
    """
    Check brackets in a string are "balanced"

    expression = string containing brackets to be checked
    """
    if not expression:
        return True

    is_open = []

    open_brackets = {"{":"}", "[":"]", "(":")"}

    close_brackets = {"}":"{", "]":"[", ")":"("}
    
    for c in expression:
        if c in open_brackets.keys():
            is_open.append(c)
        if c in close_brackets.keys():
            if is_open and is_open[-1] != close_brackets[c]:
                return False
            elif not is_open:
                return False
            is_open.pop()

    if is_open:
        return False

    return True


import unittest

class TestSolution(unittest.TestCase):
    
    def test_is_matched_empty_string(self):
        expression = "" 
        result = is_matched(expression)
        self.assertTrue(result)

    def test_is_matched_balanced(self):
        expressions = [
            "{}",
            "{}[]()",
            "{{{[[[()]]][]}}}",
        ]
        for e in expressions:
            result = is_matched(e)
            self.assertTrue(result)

    def test_is_matched_unbalanced(self):
        expressions = [
            "}{",
            "{}}",
            "[[([)]]]",
            "(((())"
        ]
        for e in expressions:
            result = is_matched(e)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
