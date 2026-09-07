import numpy as np;

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        numOfGroups = len(processorTime)
        tasks.sort()
        processorTime.sort(reverse=True)
        groups = np.array_split(tasks, numOfGroups)
        timeTaken = []

        for i, group in enumerate(groups):
            timeTaken.append(max(group + processorTime[i]))
            print(timeTaken)
        return int(max(timeTaken))
        