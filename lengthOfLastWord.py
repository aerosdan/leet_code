class Solution:
    def lengthOfLastWord(self, phrase: str) -> int:
        splitted_phrase = phrase.split(" ")
        print(phrase.split())


print(Solution().lengthOfLastWord("Hello World"))

  
print(Solution().lengthOfLastWord(" fly me   to   the moon  "))
