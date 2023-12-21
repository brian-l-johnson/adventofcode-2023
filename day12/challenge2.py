#!/usr/bin/env python3

import sys
import re

def appendAll(arr, c):
    ret = []
    for s in arr:
        ret.append(s+c)
    return ret


mc = 0
for line in sys.stdin:
    line = line.rstrip()
    parts = line.split(" ")
    conditions = parts[0]
    checks = parts[1]

    conditions = conditions+"?"+conditions+"?"+conditions+"?"+conditions+"?"+conditions
    checks = checks*5

    print(line)
    print(checks)

    candidates = [""]
    #print(f"line: {line}")
    #print(f"conditions: {conditions}")
    for cond in conditions:
        if cond in [".","#"]:
            candidates = appendAll(candidates, cond)
        elif cond == '?':
            c1 = appendAll(candidates, ".")
            c2 = appendAll(candidates, "#")
            candidates = c1+c2
    #print(candidates)
    
    check_re_str = "^\.*"
    
    for c in checks.split(","):
        check_re_str = check_re_str + "\#{"+c+"}\.+"
    check_re_str = check_re_str[:-1]+"*$"
    #print(f"regex: {check_re_str}")
    check_re = re.compile(check_re_str)
    for candidate in candidates:
        if check_re.match(candidate):
            #print(f"{candidate} matches")
            mc+=1
    print(f"{mc} matches so far")
print(mc)
    


