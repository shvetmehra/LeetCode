from bisect import bisect_left

class SegmentTree:
    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords) - 1
        self.count = [0] * (4 * self.n)
        self.covered_len = [0.0] * (4 * self.n)

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.count[v] += add
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
        
        if self.count[v] > 0:
            self.covered_len[v] = self.coords[tr + 1] - self.coords[tl]
        else:
            if tl != tr:
                self.covered_len[v] = self.covered_len[2 * v] + self.covered_len[2 * v + 1]
            else:
                self.covered_len[v] = 0

class Solution:
    def separateSquares(self, squares):
        events = []
        x_coords = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # Bottom edge
            events.append((y + l, -1, x, x + l))  # Top edge
            x_coords.add(x)
            x_coords.add(x + l)
        
        events.sort()
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        
        st = SegmentTree(sorted_x)
        
        # Pass 1: Calculate Total Area
        total_area = 0.0
        prev_y = events[0][0]
        for y, type, x1, x2 in events:
            total_area += st.covered_len[1] * (y - prev_y)
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            prev_y = y
            
        # Pass 2: Find the Y that bisects the area
        target = total_area / 2.0
        current_area = 0.0
        st = SegmentTree(sorted_x) # Reset Segment Tree
        prev_y = events[0][0]
        
        for y, type, x1, x2 in events:
            delta_area = st.covered_len[1] * (y - prev_y)
            if current_area + delta_area >= target:
                # The answer lies between prev_y and y
                remaining = target - current_area
                return prev_y + (remaining / st.covered_len[1])
            
            current_area += delta_area
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            prev_y = y
            
        return float(events[-1][0])