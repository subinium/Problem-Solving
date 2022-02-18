class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums)
        p_max, m_max = [0], [0]
        for i in nums:
            if i > 0:
                if p_max[-1] == 0:
                    p_max.append(i)
                else:
                    p_max[-1] *= i
                m_max[-1] *= i
            elif i < 0:
                p_max.append(m_max[-1]*i)
                if p_max[-2] == 0:
                    m_max.append(i)
                else:
                    m_max.append(p_max[-2]*i)
            else:
                p_max.append(0)
                m_max.append(0)
        return max(p_max)
