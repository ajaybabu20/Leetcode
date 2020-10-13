class Solution:
    def __init__(self):
        self.missed = []
        self.map = {}
        self.repeated = []

    def findErrorNums(self, nums):
        self.nums = nums
        self.repeatedvalues = list(set(self.findrepeatvalues()))
        self.missingvalue = self.findmissingvalue()
        return self.repeatedvalues.append(self.missingvalue)

    def findrepeatvalues(self):
        for i in self.nums:
            if i not in self.map:
                self.map[i] = i
            else:
                self.repeated.append(i)
        return self.repeated

    def findmissingvalue(self):
        for i in range(1, self.nums[-1] + 1):
            if i not in self.map.keys():
                self.missed.append(i)
        return self.missed
