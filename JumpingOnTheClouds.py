def jumpingOnClouds(c):
    # Write your code here
    # 0 0 0 0 1 0
    # if next value is 1 skip it
    # if next 2 values are 0 skip them
    i = 0
    counter = 0
    while i < len(c):
        if i < len(c) - 2 and c[i+1] == 1:
            i += 2
            counter += 1
        elif i < len(c) - 2 and c[i+1] == 0 and c[i+2] == 0:
            i += 2
            counter += 1
        else:
            if i == len(c) - 1:
                break
            i += 1
            counter += 1
    return counter