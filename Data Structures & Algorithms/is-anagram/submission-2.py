class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = {}
        for c in s:
            if not c in s_cnt:
                s_cnt[c] = 0
            s_cnt[c] += 1
        for c in t:
            if not c in s_cnt:
                return False
            s_cnt[c] -= 1
            if s_cnt[c] < 0:
                return False
        for k, v in s_cnt.items():
            if v != 0:
                return False
        return True