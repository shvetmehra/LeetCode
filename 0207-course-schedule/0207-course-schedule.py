from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList = [[] for _ in range (numCourses)]
        inDegree = [0 for _ in range (numCourses)]

        for u,v in prerequisites:
            adjList[u].append(v)
            inDegree[v] +=1
        queue = deque()
        result = []

        for i in range (0,numCourses):
            if inDegree[i]==0:
                queue.append(i) 

        while len(queue)!=0:
            currentNode = queue.popleft()
            result.append(currentNode)

            for adjNode in adjList[currentNode]:
                inDegree[adjNode] -= 1
                if inDegree[adjNode]==0:
                    queue.append(adjNode)
        if len(result)==numCourses:
            return True
        return False  
        