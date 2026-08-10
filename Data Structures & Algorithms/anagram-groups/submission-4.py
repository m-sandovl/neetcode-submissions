class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        for word in strs:
            counts = [0] *26
            for letter in word:
                counts[ord(letter) - ord('a')] +=1 
                key = tuple(counts)
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())