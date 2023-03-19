# Task
# You are given a string S
# Your task is to find the first occurrence of an alphanumeric character in S
# (read from left to right) that has consecutive repetitions.
# Input Format:
# A single line of input containing the string S.
# Constraints: 0<len(S)<100
# Output Format: 
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.


# Task solving:

import re

S = input().strip()
# S1 = '..12345678910111213141516171820212223'
# S2 = 'qwertpuu'
m = re.search(r'([A-Za-z0-9])\1+', S)
print(m.group(1) if m else -1)


############################################
# Next task solving:

# import re

# S = 'raabcreEEfgyYhFjkIooOmaanprtt'
# S1 = 'abaabaabaabaae'
# match = re.findall(r'[^AaEeUuIiOo+-0-9]([AaEeUuIiOo]{2,})(?=[^AaEeUuIiOo+-0-9])', S1)
# print(match)
# print('\n'.join(match) if match else -1)


###########################################
# Re.start() & Re.end() task solving:

import re

S = input().strip()
k = input().strip()

flag = False
start = 0
end = start + len(k)
s_temp = S[start:end]
while len(S) >= end :    
    m = re.match(k, s_temp)
    if m:
        flag = True
        print((start, end - 1))
        start += 1
        end += 1      
    else:
        start +=  1
        end += 1
    s_temp = S[start:end]
if not flag:
    print((-1, -1))

##########################################
# Regex Substitution
#Task:
#You are given a text of lines. The text contains && and || symbols.
#Your task is to modify those symbols to the following:
#&& → and
#|| → or
#Both && and || should have a space " " on both sides.

import re

N = int(input())
text = list()
for index in range(N):
    text.append(
        re.sub(r'(?<= )\|\|(?= )', 'or', (
            re.sub(r'(?<= )\&\&(?= )', 'and', input()))))
print('\n'.join(text))