class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def word_count(s):
            cnt = dict()
            for c in s:
                if not c in cnt:
                    cnt[c] = 0
                cnt[c] += 1
            return cnt
        def match_wc(cnt1, cnt2):
            if len(cnt1) != len(cnt2):
                return False
            for k1, v1 in cnt1.items():
                if not k1 in cnt2 or cnt2[k1] != v1:
                    return False
            return True
        groups = []
        for s in strs:
            cnt = word_count(s)
            for g in groups:
                if match_wc(g[0], cnt):
                    g[1].append(s)
                    break
            else:
                groups.append((cnt, [s]))
        return [g[1] for g in groups]