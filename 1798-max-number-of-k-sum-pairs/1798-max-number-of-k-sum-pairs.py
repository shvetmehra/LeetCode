class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        ans = 0
        for i in nums:
            if k//2 == i and k%2 == 0:
                pair = min(count[i], count[k-i])
                ans += pair//2
                count[i]=0
                count[k-i]=0
            elif count[i]!=0:
                if k-i in count and count [k-i]!=0:
                    ans +=1
                    count[k-i]-=1
                    count[i]-=1
        return ans