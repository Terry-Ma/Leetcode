class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to_map = {}
        for src, dst in tickets:
            if src not in from_to_map:
                from_to_map[src] = [dst]
            else:
                from_to_map[src].append(dst)
        for src in from_to_map:
            from_to_map[src].sort()
        path = ['JFK']
        n = len(tickets)
        self.dfs(path, from_to_map, n)

        return path

    def dfs(self, path, from_to_map, n):
        if len(path) == n + 1:
            return True
        elif path[-1] not in from_to_map or not from_to_map[path[-1]]:
            return False
        src = path[-1]
        for i in range(len(from_to_map[src])):
            path.append(from_to_map[src][i])
            from_to_map[src].pop(i)
            if self.dfs(path, from_to_map, n):
                return True
            from_to_map[src].insert(i, path[-1])
            path.pop()
        return False
