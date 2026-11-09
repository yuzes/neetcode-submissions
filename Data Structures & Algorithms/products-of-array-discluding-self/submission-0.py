class Solution:
    # productExceptSelf = evey element on the left * evey element on the right
    # result[i] = product[0:i-1] * product[i+1:-1]
    # prefix[i - 1] = product[0:i - 1]
    # postfix[i + 1] = product[i + 1: -1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        product = 1
        for i in range(len(nums)):
            prefix[i] = product * nums[i]
            product *= nums[i]
        product = 1
        for i in reversed(range(len(nums))):
            postfix[i] = product * nums[i]
            product *= nums[i]
        res = [0] * n
        res[0] = postfix[1]
        res[n - 1] = prefix[n-2]
        for i in range(1, n-1):
            res[i] = prefix[i-1] * postfix[i + 1]
        return res