class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        stack = [0]
        visited.add(0)
        while stack:
            room = stack.pop()
            visited.add(room)
            for x in rooms[room]:
                if x not in visited:
                    stack.append(x)
        return len(visited)==len(rooms)