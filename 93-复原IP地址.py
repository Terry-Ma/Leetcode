class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(si, num, memory_map):
            result = []
            memory_map[(si, num)] = result
            if not (num <= len(s) - si <= 3 * num):  # 剪枝1
                return
            cur_num = 0
            for step in range(3):
                if si + step < len(s):
                    cur_num = 10 * cur_num + int(s[si + step])
                    if cur_num <= 255:  # 剪枝2
                        if (si + step + 1, num - 1) not in memory_map:
                            dfs(si + step + 1, num - 1, memory_map)
                        for sub_list in memory_map[(si + step + 1, num - 1)]:
                            result.append(sub_list + [s[si:si+step + 1]])
                if s[si] == '0':  # 防止前导零
                    break

        memory_map = {}
        memory_map[(len(s), 0)] = [['']]
        dfs(0, 4, memory_map)
        reverse_res = memory_map[(0, 4)]
        total_res = []
        for res in reverse_res:
            cur_ip_str = res[-1]
            for i in range(3, 0, -1):
                cur_ip_str += '.{}'.format(res[i])
            total_res.append(cur_ip_str)

        return total_res
