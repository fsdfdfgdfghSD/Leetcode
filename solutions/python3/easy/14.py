from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: List[str] = []

        strs.sort()
        
        first = strs[0]
        last = strs[len(strs) - 1]

        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix.append(first[i])
            else:
                break

        return "".join(prefix)