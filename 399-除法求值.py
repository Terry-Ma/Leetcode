class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        weight_dict = {}
        src2dst = {}
        res = []
        for i in range(len(values)):
            x1, x2 = equations[i]
            value = values[i]
            weight_dict[(x1, x2)] = value
            weight_dict[(x2, x1)] = 1 / value
            if x1 in src2dst:
                src2dst[x1].append(x2)
            else:
                src2dst[x1] = [x2]
            if x2 in src2dst:
                src2dst[x2].append(x1)
            else:
                src2dst[x2] = [x1]
        for query in queries:
            src, dst = query
            node_set = set()
            res.append(self.query_val(src, dst, weight_dict, src2dst, node_set))

        return res

    def query_val(self, src, dst, weight_dict, src2dst, node_set):
        if src not in src2dst or dst not in src2dst:
            return -1
        if src == dst:
            return 1
        node_set.add(src)
        for next_src in src2dst[src]:
            if next_src not in node_set:
                val = self.query_val(next_src, dst, weight_dict, src2dst, node_set)
                if val != -1:
                    src2dst[src].append(dst)
                    src2dst[dst].append(src)
                    weight_dict[(src, dst)] = weight_dict[(src, next_src)] * val
                    weight_dict[(dst, src)] = 1 / (weight_dict[(src, next_src)] * val)
                    return weight_dict[(src, next_src)] * val

        return -1
