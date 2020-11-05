from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    	
    	index = 0
    	max_length = releaseTimes[0]

    	for i in range(len(releaseTimes) - 1):
    		length = releaseTimes[i+1] - releaseTimes[i]
    		if length >= max_length:
    			if length > max_length or length == max_length and ord(keysPressed[i+1]) > ord(keysPressed[index]):
    				index = i+1
    			max_length = length
    			
    	return keysPressed[index]


releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"

releaseTimes=[9,29,49,50]
keysPressed="cbcd"

solution = Solution()
print(solution.slowestKey(releaseTimes, keysPressed))