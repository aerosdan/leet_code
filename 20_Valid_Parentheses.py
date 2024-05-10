class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = ['(', ')', '{', '}', '[', ']']
        for char in valid_chars:
            a = s.count(char)
            print(f"char {char} has {a}")

print(Solution().isValid("()[]{}"))
