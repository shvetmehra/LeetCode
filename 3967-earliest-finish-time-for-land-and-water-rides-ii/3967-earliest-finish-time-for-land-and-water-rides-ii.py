from typing import List
from bisect import bisect_right

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def solve(firstStart, firstDur, secondStart, secondDur):
            rides = sorted(zip(secondStart, secondDur))

            starts = [s for s, d in rides]
            durs = [d for s, d in rides]

            m = len(rides)

            prefixMinDur = [0] * m
            prefixMinDur[0] = durs[0]

            for i in range(1, m):
                prefixMinDur[i] = min(prefixMinDur[i - 1], durs[i])

            suffixMinFinish = [0] * m
            suffixMinFinish[-1] = starts[-1] + durs[-1]

            for i in range(m - 2, -1, -1):
                suffixMinFinish[i] = min(
                    suffixMinFinish[i + 1],
                    starts[i] + durs[i]
                )

            ans = float('inf')

            for s, d in zip(firstStart, firstDur):
                finish = s + d

                idx = bisect_right(starts, finish) - 1

                if idx >= 0:
                    ans = min(
                        ans,
                        finish + prefixMinDur[idx]
                    )

                if idx + 1 < m:
                    ans = min(
                        ans,
                        suffixMinFinish[idx + 1]
                    )

            return ans

        return min(
            solve(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration
            ),
            solve(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration
            )
        )