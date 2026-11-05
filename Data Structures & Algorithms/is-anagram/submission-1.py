class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_size = ord('z') - ord('a') + 1
        s_hash = [0] * list_size
        t_hash = [0] * list_size

        self.get_hash(s_hash, s)
        self.get_hash(t_hash, t)

        return s_hash == t_hash

    def get_hash(self, hash_list: list, word: str):
        for char in word:
            hash_list[ord(char) - ord('a')] += 1