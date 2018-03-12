import numpy

hugeNumber = float("inf")

stages = 12
startInventory = 3
inventoryCapacity = 20

setupCost = 1.5
holdingCost = 0.5
demand = numpy.array([-1000, 4, 6, 5, 6, 8, 3, 4, 2, 8, 5, 4, 3])  

f = numpy.zeros([stages + 2, inventoryCapacity + 1])
x = numpy.zeros([stages + 1, inventoryCapacity + 1], dtype=int)

for t in range(stages, 0, -1):
	for i in range(inventoryCapacity + 1):

		minOrder = 0
		maxOrder = inventoryCapacity - i + demand[t]

		value = hugeNumber

		for d in range(minOrder, maxOrder):

			j = i + d - demand[t]
			orderCost = 0
			if d == 0:
				orderCost = orderCost
			if d < 5:
				orderCost = setupCost + d * 10
			elif d >= 5:
				orderCost = setupCost + d * 9

		moveValue = holdingCost * j + orderCost + f[t + 1, j]

if moveValue < value:
value = moveValue
bestMove = d

# End of p loop

f[t, i] = value
x[t, i] = bestMove

# End of i loop

# End of t loop

print("Optimal cost is " + str(f[1, startInventory]))

