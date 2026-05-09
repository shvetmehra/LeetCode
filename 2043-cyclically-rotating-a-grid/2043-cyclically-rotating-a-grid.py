class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 1. Determining the Number of Layers
        # 2. Layer Traversal 
        # 3. Add elements to array then rotate array 
        # 4. Fill the Grid again
        # for example if we have grid 4 * 6 so the 1st layer will occupy 2 rows and 2 cols. Now we will be left with 2*4.
        # m/2 & n/2 No of layers m = 6/2 =3 and n = 4/2 = 2: We will pick minimum
        # Top Row, bottom row, left col, right col
        # Top row = layer[starting from 0]; bottom row = m-1-layer; left col = layer[starting form 0]; right col = n-1-layer.
        m = len(grid)
        n = len(grid[0])
        layers = min(m,n)//2

        for layer in range(layers):
            top = layer        
            bottom = m-layer-1
            left = layer
            right = n-layer-1

            # Extract elements
            elements = []

            for col in range (left, right+1): #Top Row
                elements.append(grid[top][col])
            for row in range (top+1, bottom+1): #Right Col
                elements.append(grid[row][right])

            if bottom>top:
                for col in range(right -1, left-1, -1): # Bottom Row
                    elements.append(grid[bottom][col])
            if right>left:
                for row in range(bottom-1, top, -1): # Left Col
                    elements.append(grid[row][left])
            #Rotation:
            rotation = k%len(elements)
            rotated = elements[rotation:] + elements[:rotation] if rotation else elements
            #Fill the grid back with rotated elements
            idx = 0
            for col in range (left, right+1): # top
                grid[top][col]= rotated[idx]
                idx+=1
            for row in range (top+1, bottom+1): # right
                grid[row][right]= rotated[idx]
                idx +=1
            if bottom>top:
                for col in range (right-1, left-1, -1): #bottom
                    grid[bottom][col] = rotated[idx]
                    idx +=1
            if right>left:
                for row in range (bottom-1, top, -1): # left
                    grid[row][left]= rotated[idx]
                    idx+=1
        return grid