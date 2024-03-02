#!/usr/bin/python3
""" Log parsing DSA """
import fileinput


i = 0
size = 0
dataMap = {}
data = fileinput.input()

try:
    for line in data:
        if i == 10:
            i = 0
            print(f"File size: {size}")
            for key, value in sorted(dataMap.items()):
                print(f"{key}: {value}")
        sep = line.rstrip().split(" ")
        if len(sep) != 9:
            continue
        try:
            statCode = int(sep[-2])
            line = int(sep[-1])
        except Exception:
            continue
        if statCode not in dataMap:
            dataMap[statCode] = 1
        else:
            dataMap[statCode] += 1
        size += line
        i += 1

except Exception:
    pass

finally:
    print(f"File size: {size}")
    for key, value in sorted(dataMap.items()):
        try:
            print(f"{int(key)}: {value}")
        except Exception:
            pass
