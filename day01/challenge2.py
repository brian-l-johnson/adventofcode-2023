import sys
import re

sum = 0

numberdict = {
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


for line in sys.stdin:
  line = line.rstrip()
  print(f'got line --{line}--')
  nums = numberify(line)
  print(f'transformed line: {nums}') 
  cal = nums[0]*10+nums[len(nums)-1]
  sum = sum + cal
  
  
print("Done")
print(f'got total: {sum}')