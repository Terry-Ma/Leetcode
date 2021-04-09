class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        src2dst = defaultdict(list)
        n = 0
        for edge in edges:
            src2dst[edge[0]].append(edge[1])
            src2dst[edge[1]].append(edge[0])
            n = max(n, edge[1])
        node_state = [0] * (n + 1)
        path = [1]
        src = 1
        node = self.dfs(src2dst, src, node_state, path)
        edge_set = set()
        edge_set.add((min(path[-2], node), max(path[-2], node)))
        for i in range(len(path) - 2, -1, -1):
            if path[i] == node:
                break
            edge_set.add((min(path[i - 1], path[i]), max(path[i - 1], path[i])))
        # print(edge_set)
        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0], edges[i][1]) in edge_set:
                return edges[i]

    def dfs(self, src2dst, src, node_state, path):
        # print(src, path, node_state[src])
        if node_state[src] == 1:
            return src
        node_state[src] = 1
        for dst in src2dst[src]:
            if node_state[dst] != 2 and (len(path) < 2 or dst != path[-2]):
                path.append(dst)
                pre = src
                res = self.dfs(src2dst, dst, node_state, path)
                if res != -1:
                    return res
                path.pop()
        node_state[src] = 2

        return -1
