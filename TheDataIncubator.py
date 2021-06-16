# TheDataIncubator.py (Python v3)
# -----------------
#
# Doug Woolridge
# 6/16/2021
# Rev 1.0
#
# This program takes float (or integer) numbers from StdIn and
# outputs to StdOut the running Average, Standard Deviation, and
# Median (using the average method for even sample sets)
#
# Outputs:  (Average),(Standard Deviation),(Median)
#
# -----------------
import sys

total =   0
linenum = 0
dataSet = []

for inLine in sys.stdin:
  linenum += 1
  try:
    thisNum = float(inLine)
  except:
    print("Non-numeric input in line "+str(linenum)+": "+inLine)
    break

  # Add to dataset
  total += thisNum
  dataSet.append(thisNum)

  # Average (mean)
  mean = total / linenum

  # StdDev
  stdDev = 0
  for x in dataSet:
    stdDev += (x-mean)**2

  stdDev = stdDev / (len(dataSet))
  stdDev = stdDev**0.5

  # Median
  if (len(dataSet) % 2) == 0:
    # Even
    median = (dataSet[int(len(dataSet)/2)] + dataSet[int(len(dataSet)/2)-1]) / 2
  else:
    # Odd
    median = dataSet[int(len(dataSet)/2)]

  print(format(mean,"0.3f")+","+format(stdDev,"0.3f")+","+format(median,"0.3f"))
