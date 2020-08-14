import math

def guessPowerSum(X, N):
    limit = X**(1./N)
    units = [y for y in [x**N for x in range(1, math.ceil(limit)+1)] if y<=X]
    unitSum = []

    for i in range(0, len(units)):
        unitSum.append(units[i])
        for j in range(0, len(unitSum)-1):
            addSum = unitSum[j] + units[i]
            if addSum <= X:
                unitSum.append(addSum)

    return unitSum.count(X)

print(guessPowerSum(800, 2))


# Line 6:
# - using only ceil() without +1 misses upper bound e.g. x=100, n=2
# - use (~alias) y to avoid repeated evaluation of x**N which must be < X

# Two Critical Missteps
# 1. On line 10, initially used len(0,len()) instead of len(0,len()-1) then
# trying to remove double-self-add (e.g. 1+1 or 4+4) via checking whether unitSum[j]==units[i]
# which ends up removing a horde of numbers that happen to have equal value but one is made
# up of smaller units
# 2. Idiotically used extra else-clause with 'break' under line 12-13

# needs Python3
