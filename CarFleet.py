def carFleet(target, position, speed):
    n = len(position)
    posByTime = {}
    for i in range(n):
        posByTime[position[i]] = int((target - position[i]) / speed[i])

    currMaxT = 0
    fleetCount = 0
    for p in range(target - 1, -1, -1):
        if p in posByTime:
            t = posByTime[p]
            if t > currMaxT:
                currMaxT = t
                fleetCount += 1
    return fleetCount


print(carFleet(20, [6, 2, 17], [3, 9, 2]))
