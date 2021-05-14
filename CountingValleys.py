def countingValleys(steps, path):
    # Write your code here
    # UDDDUDUU
    # UUUUDDDDDU
    # DDDDDDUUUUUUDU
    cnt = 0
    valleyCount = 0
    for step in path:
        if step == "U": cnt += 1
        if step == "D": cnt -= 1
        if cnt == 0 and step == "U": valleyCount += 1
    return valleyCount