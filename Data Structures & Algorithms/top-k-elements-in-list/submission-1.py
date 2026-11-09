class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # observed that higher frequent is len(nums)
        # use bucket to store value where bucket[i] is a list of num that
        # occurs i time
        bucket = [[] for _ in range(len(nums) + 1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            bucket[count].append(num)
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result