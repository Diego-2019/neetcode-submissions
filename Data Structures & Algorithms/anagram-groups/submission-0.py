class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]

        anagrams = defaultdict(list)
        for word in strs:
            anagrams[self.get_hash(word)].append(word)
        return list(anagrams.values())

    def get_hash(self, word) -> Tuple[int, ...]:
        hash = [0] * 26
        for letter in word:
            hash[ord(letter) - ord('a')] += 1
        return tuple(hash)