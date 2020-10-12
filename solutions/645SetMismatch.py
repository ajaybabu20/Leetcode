class Solution:

    def findErrorNums(self, nums):
        self.nums = nums

    def findrepeatvalues(self):
        self.map = {}
        self.repeated = []
        for i in self.nums:
            if i not in self.map:
                self.map[i] = i
            else:
                self.repeated.append(i)
        return self.repeated

    def findmissingvalue(self):
        self.missingvalue = []
        for i in range(1,self.nums[-1] + 1):
            if i not in self.map.keys():
                self.missingvalue.append(i)
        return self.missingvalue


sol = Solution()
sol.findErrorNums(
    [1,2,2,4])

repeatedvalues = list(set(sol.findrepeatvalues()))
print(repeatedvalues)
missingvalues = sol.findmissingvalue()
print(missingvalues)
repeatedvalues.append(missingvalues)
print(repeatedvalues)
