from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        hashmap = defaultdict(list)
        for index, val in enumerate(arr):
            hashmap[val].append(index)
        queue = deque([0])
        steps = 0
        visited = set()
        
        visited.add(0)
        while queue:
            queue_len = len(queue)
            for  _ in range (queue_len):
                index = queue.popleft()
                if index == len(arr)-1:
                    return steps
                for adj_index in hashmap.get(arr[index], []):
                    if adj_index not in visited:
                        queue.append(adj_index)
                        visited.add(adj_index)
                hashmap[arr[index]]=[]
                
                if (index-1 >-1) and (index -1) not in visited:
                        queue.append(index-1)
                        visited.add(index-1)
                if (index+1 <len(arr)) and (index +1) not in visited: 
                        queue.append(index+1)
                        visited.add(index+1)
            steps +=1
        return -1