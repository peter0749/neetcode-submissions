from collections import Counter

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.par[x] == x:
            return x
        return self.find(self.par[x])
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        elif self.rank[px] > self.rank[py]:
            self.par[py] = px
        else:
            self.rank[px] += 1
            self.par[py] = px

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uniq_nums = list(set(nums)) # hashset O(n)
        uf = UnionFind(len(uniq_nums))
        num_inv_index = dict()
        for i, n in enumerate(uniq_nums):
            num_inv_index[n] = i
        for i, n in enumerate(uniq_nums):
            if n+1 in num_inv_index:
                uf.union(i, num_inv_index[n+1])
        all_par = [uf.find(i) for i in range(len(uniq_nums))]
        cnt = Counter(all_par)
        return cnt.most_common(1)[0][1]