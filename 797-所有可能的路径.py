class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        cur_path = [0]
        res = []
        self.dfs(graph, 0, cur_path, res)

        return res

    def dfs(self, graph, cur_node, cur_path, res):
        if cur_node == len(graph) - 1:
            res.append(cur_path[:])
        else:
            if cur_node < len(graph):
                for node in graph[cur_node]:
                    cur_path.append(node)
                    self.dfs(graph, node, cur_path, res)
                    cur_path.pop()
