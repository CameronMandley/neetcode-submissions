class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempstack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            if len(tempstack) == 0 or tempstack[-1][0] >= curr_temp:
                tempstack += [(curr_temp, i)]
            else:
                while len(tempstack) != 0 and tempstack[-1][0] < curr_temp:
                    prev_temp = tempstack.pop()
                    result[prev_temp[1]] = i - prev_temp[1]
                tempstack += [(curr_temp, i)]
        return result
        