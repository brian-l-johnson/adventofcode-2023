import sys
import re

sum = 0

numberdict = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def numberify(s):
  parsed = []
  for i in range(len(s)):
    if re.match(r"\d", s[i]):
      parsed.append(int(s[i]))
    else:
      for k in numberdict:
        if len(s[i:]) >= len(k):
          candidate = s[i:i+len(k)]
          if candidate == k:
            parsed.append(numberdict[k])
  return parsed

def find_first_num(s):
  for i in range(len(s)):
    for k in numberdict:
      if len(s[i:]) >= len(k):
        if k == s[i:i+len(k)]:
          return numberdict[k]

def find_last_num(s):
  for i in reversed(range(len(s))):
    for k in numberdict:
      if i - len(k) >= 0:
        if k == s[i-len(k):i]:
          return numberdict[k]



for line in sys.stdin:
  sum = sum + 10*find_first_num(line)+find_last_num(line)
  
  
print("Done")
print(f'got total: {sum}')