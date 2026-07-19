class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s):d}#{s:s}')
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        ret = []
        p0, p1 = 0, 0
        while p1 < len(s):
            if s[p1] == '#':
                n = int(s[p0:p1])
                ret.append(s[p1+1:p1+1+n])
                p0 = p1+1+n
                p1 = p0
            p1 += 1
        return ret