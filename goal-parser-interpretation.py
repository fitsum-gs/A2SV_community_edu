class Solution:
    def interpret(self, command: str) -> str:
        answer = ''
        i = 0
        while i < len(command):
            if command[i] == "G":
                answer += "G"
                i += 1
            elif command[i:i+2] == "()":
                answer += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                answer += "al"
                i += 4
        return answer
#https://leetcode.com/problems/goal-parser-interpretation/
