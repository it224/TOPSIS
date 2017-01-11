#!/usr/bin/env python
import math

places = ("Bali", "Bibione", "Karibik")

# dataset = ( travel expenses( Bali(tom,Petr, Jan), Bibione(tom,Petr, Jan), Karibik(tom,Petr, Jan)), 
#   accommodation expenses( Bali(tom,Petr, Jan), Bibione(tom,Petr, Jan), Karibik(tom,Petr, Jan)),
#   entertainment( Bali(tom,Petr, Jan), Bibione(tom,Petr, Jan), Karibik(tom,Petr, Jan)),
#   swimming quality( Bali(tom,Petr, Jan), Bibione(tom,Petr, Jan), Karibik(tom,Petr, Jan) ) )
dataset = (
  ( (6,2,4),(5,2,2),(1,1,1) ),   # travel expenses
  ( (8,8,5),(6,2,4),(3,2,4) ),   # accommodation expenses
  ( (4,2,3),(9,9,3),(9,9,9) ),   # entertainment
  ( (4,5,6),(2,1,3),(10,10,7) )    # swimming quality
)


# weights, criterions = [ travel expenses[Bali, Bibione, Karibik],
#   accommodation expenses[Bali, Bibione, Karibik],
#   entertainment[Bali, Bibione, Karibik],
#   swimming quality[Bali, Bibione, Karibik] ]
weights = [
  [0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0]
]

criterions = [
  [0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0]
]

# sumMinMaxDiff, minMaxDiff = [ Bali[minDiff, Maxdiff], Bibione[minDiff, Maxdiff], Karibik[minDiff, Maxdiff]]
sumMinMaxDiff = [
  [0.0, 0.0],
  [0.0, 0.0],
  [0.0, 0.0]
]

minMaxDiff = [
  [0.0, 0.0],
  [0.0, 0.0],
  [0.0, 0.0]
]

# final = [ Bali, Bibione, Karibik ]
final = [0.0, 0.0, 0.0]


# Caliculate weights
for i in range(len(dataset)):
  for j in range(len(dataset[i])):
    weights[i][j] = float(sum(dataset[i][j])/len(dataset[i]))


# Normalized matrix
for i in range(len(weights)):
  for j in range(len(weights[i])):
    criterions[i][j] = math.pow(weights[i][j], 2) / sum(weights[i])

# Calcurate min/max differences and add up
for i in criterions:
  for j in range(len(i)):
    sumMinMaxDiff[j][0] += math.pow(i[j]-min(i), 2)
    sumMinMaxDiff[j][1] += math.pow(i[j]-max(i), 2)

# calculate Sqrt
for i in range(len(sumMinMaxDiff)):
  for j in range(len(sumMinMaxDiff[i])):
    minMaxDiff[i][j] = math.sqrt(sumMinMaxDiff[i][j])

# Compute the realtive closest solution
for i in range(len(minMaxDiff)):
  final[i] = minMaxDiff[i][0]/sum(minMaxDiff[i])

print "Ideal Alternative -> Negative Ideal Alternative"
print places[final.index(max(final))]

