class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        records = []
        for i in range(len(operations)):
            if operations[i] == '+':
                records.append(records[-1] + records[-2])
            elif operations[i] == 'D':
                records.append(records[-1] * 2)
            elif operations[i] == 'C':
                records.pop()
            else:
                records.append(int(operations[i]))
        return sum(records)
