def stair(n, counter = [0]):
    if n == 0:
        counter[0] += 1
    if n < 0 :
        return 
    else:
        stair(n-1)
        stair(n-2)
        stair(n-3)
    return counter[0]

n = 4
print ('If staircase has {} steps, there would be {} possible ways.'.format(n, stair(n)))