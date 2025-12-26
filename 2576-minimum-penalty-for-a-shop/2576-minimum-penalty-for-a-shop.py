class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n=len(customers)
        y_cus = 0

        for i in range (n):
            if customers[i]=='Y':
                y_cus +=1
        
        min_penalty = float('inf')
        hours = 0
        y_found = 0
        n_found = 0

        for j in range (n+1):  
            y_remain = y_cus - y_found
            penalty = y_remain + n_found

            if penalty < min_penalty:
                hours = j
                min_penalty = penalty
            if j<n:
                if customers[j] == 'N':
                    n_found +=1
                else:
                    y_found +=1
        return hours
        