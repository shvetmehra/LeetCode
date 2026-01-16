class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums += nums
        n = len(nums)
        ans = [-1]*n
        st = []

        for i in range (n-1, -1, -1):
            while len(st)>0 and nums[i]>= st[-1]:
                st.pop()
            if len(st)==0:
                ans[i] =-1
            else:
                ans[i]= st[-1]
            st.append(nums[i])

        return ans[:len(ans)//2]
        