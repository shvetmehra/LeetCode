class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []
        l, r = 0, len(products) - 1
        
        for i in range(len(searchWord)):
            char = searchWord[i]
            
            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1
            
            suggestions = []
            remain = r - l + 1
            for j in range(min(3, remain)):
                suggestions.append(products[l + j])
                
            res.append(suggestions)
            
        return res