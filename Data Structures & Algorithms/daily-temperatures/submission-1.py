class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempstack = []
        results = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if len(tempstack) == 0 or tempstack[-1][0] > temperatures[i]:
                tempstack += [(temperatures[i], i)]
            else:
                while len(tempstack) != 0 and tempstack[-1][0] < temperatures[i]:
                    prev_temp, index = tempstack.pop()
                    results[index] = i - index
                tempstack += [(temperatures[i], i)]

                
        return results
        