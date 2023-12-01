import sys
import re

sum = 0

for line in sys.stdin:
  line = line.rstrip()
  numbers = re.sub(r"[^0-9]", "", line)
  cal = int(numbers[0]+numbers[len(numbers)-1])
  sum = sum + cal
    
print("Done")
print(f'got total: {sum}')