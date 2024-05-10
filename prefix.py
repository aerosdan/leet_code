from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        common_prefix = ''
        for n in range(1, len(shortest_word)+1):
            abc = [word[:n] for word in strs]
            same = all(elem == abc[0] for elem in abc)
            if same:
                common_prefix = abc[0]
                continue
            else:
                break
        return common_prefix

abc = ["flower", "flow", "flight"]
nnn = ["a", "a", "a"]
nnn = ["a", "b", "a"]

aaa = ["dog","racecar","car"]
bbbb = ['a']
a = Solution().longestCommonPrefix(bbbb)
print('result:', a)

