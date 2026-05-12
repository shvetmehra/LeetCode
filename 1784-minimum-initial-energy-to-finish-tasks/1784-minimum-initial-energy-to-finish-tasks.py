class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: (x[1]-x[0]), reverse = True)
        energy = 0
        ans = 0
        for actual, minimum in tasks:
            if energy < minimum:
                extra_energy = minimum - energy
                ans+= extra_energy
                energy += extra_energy
            energy -= actual
        return ans
        