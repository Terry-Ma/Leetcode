class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''

        path_stack = []
        index = 0
        while index < len(path):
            if path[index] != '/':
                cur_path_list = []
                while index < len(path) and path[index] != '/':
                    cur_path_list.append(path[index])
                    index += 1
                cur_path = ''.join(cur_path_list)
                if cur_path == '..':
                    if path_stack:
                        path_stack.pop()
                elif cur_path != '.':
                    path_stack.append(cur_path)
            else:
                index += 1

        return '/' + '/'.join(path_stack)
