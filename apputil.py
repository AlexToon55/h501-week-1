

# Week 1 Exercise 1
def palindrome(word) -> bool:
    s = "".join(filter(str.isalnum, word)).lower()
    return s == s[::-1]


# Week 1 Exercise 2
def parentheses(string: str) -> bool:
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0