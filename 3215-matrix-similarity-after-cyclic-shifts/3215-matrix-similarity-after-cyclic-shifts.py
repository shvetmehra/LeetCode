class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        cols = len(mat[0])
        if k % cols == 0:
            return True
        effective_K = k % cols

        for rows in mat:
            for j in range (cols):
                if rows[j] != rows[(j + effective_K)%cols]:
                    return False            
        return True