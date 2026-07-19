class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count num freq
        cnt = dict()
        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
        max_freq = max(v for v in cnt.values())
        # bucket sort
        buckets = [[] for _ in range(max_freq+1)]
        for n,f in cnt.items():
            buckets[f].append(n)
        # return top-k most frequent elements
        ret = []
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        return ret