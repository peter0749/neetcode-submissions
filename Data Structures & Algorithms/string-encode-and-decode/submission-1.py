class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(s)) for s in strs]
        metadata = ' '.join(lengths)
        return metadata + '#' + ''.join(strs)
    def decode(self, s: str) -> List[str]:
        # empty
        if s[0] == '#':
            return []
        metadata, payload = s.split('#', 1)
        lengths = list(map(int, metadata.split(' ')))
        ptr = 0
        ret = []
        for l in lengths:
            ret.append(payload[ptr:ptr+l])
            ptr += l
        return ret