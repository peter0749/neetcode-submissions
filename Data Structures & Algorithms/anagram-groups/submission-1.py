class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def make_word_count_arr(s):
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            return tuple(cnt)
        
        groups = dict()
        for s in strs:
            wc = make_word_count_arr(s)
            if wc in groups:
                groups[wc].append(s)
            else:
                groups[wc] = [s]
        return [v for v in groups.values()]