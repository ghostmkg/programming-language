def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    fuel = 0
    start_sta = -1
    for i in range(len(gas)):
        fuel = fuel + gas[i] - cost[i]
        if fuel < 0:
            start_sta = i+1
            fuel = 0
    return start_sta if fuel >= 0 else -1

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
# The function canCompleteCircuit determines the starting gas station index
# from which a vehicle can complete a circular route given the gas available
# at each station and the cost to travel to the next station. If it's not possible
# to complete the circuit, it returns -1.