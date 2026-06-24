class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        
        if n == 1:
            return M
            
        size = 2 * M
        
        base_vector = [0] * size
        for v2 in range(M):
            base_vector[v2] = v2                 
            base_vector[M + v2] = M - 1 - v2     
            
        if n == 2:
            return sum(base_vector) % MOD
            
        T = [[0] * size for _ in range(size)]
        for v in range(M):
            for vp in range(v):
                T[M + vp][v] = 1
            for vp in range(v + 1, M):
                T[vp][M + v] = 1

        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(matrix, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
                
            base = matrix
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T_pow = power(T, n - 2)
        
        final_vector = [0] * size
        for i in range(size):
            for j in range(size):
                final_vector[i] = (final_vector[i] + T_pow[i][j] * base_vector[j]) % MOD
                
        return sum(final_vector) % MOD