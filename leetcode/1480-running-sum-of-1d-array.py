import numpy as np


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return np.cumsum(nums).tolist()
