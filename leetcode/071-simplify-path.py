class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        ret = []
        for dir_name in dirs:
            if dir_name in ['', '.']:
                continue
            if dir_name == '..':
                if len(ret):
                    ret.pop()
            else:
                ret.append(dir_name)

        return '/'+'/'.join(ret)
