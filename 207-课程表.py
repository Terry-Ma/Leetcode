class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_state = [0] * numCourses
        src2dst = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            src2dst[src].append(dst)
        for src in range(numCourses):
            if not node_state[src]:
                if not self.dfs(src2dst, src, node_state):
                    return False

        return True

    def dfs(self, src2dst, src, node_state):
        node_state[src] = 1
        for dst in src2dst[src]:
            if node_state[dst] == 1:
                return False
            if node_state[dst] != 2:
                if not self.dfs(src2dst, dst, node_state):
                    return False
        node_state[src] = 2

        return True
