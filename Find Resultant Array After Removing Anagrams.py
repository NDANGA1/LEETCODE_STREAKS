from typing import List
# --------------------------------------------------------------------
# Problem: 2273. Find Resultant Array After Removing Anagrams
#
# Given a list of lowercase words, repeatedly remove any word that is
# an anagram of the one immediately before it. Continue until no two
# adjacent words are anagrams. The order of removals does not affect
# the final result.
#
# Example:
#   Input:  ["abba","baba","bbaa","cd","cd"]
#   Output: ["abba","cd"]
#
# Explanation:
#   - "baba" and "abba" are anagrams → remove "baba"
#   - "bbaa" and "abba" are anagrams → remove "bbaa"
#   - "cd" and "cd" are anagrams → remove one "cd"
#   Result = ["abba", "cd"]

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=len(words)-1
        while i>0:
            if sorted(words[i])==sorted(words[i-1]):
                words.pop(i)
            i-=1
        return words
