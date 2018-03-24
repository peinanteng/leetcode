class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        summary = {}
        for i in range(len(ppid)):
            summary[ppid[i]] = summary.get(ppid[i], []) + [pid[i]]
        res = []
        stack = [kill]
        while stack:
            cur = stack.pop()
            res.append(cur)
            if cur in summary:
                stack += summary[cur]
        return res

