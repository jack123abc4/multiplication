import random
import math

def clearConsole():  
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

NUM_FACTS = 50
MIN_MULTIPLIER = 0
MAX_MULTIPLIER = 10
WEIGHTING = {
  0:-5,
  1:-5,
  7:5,
  8:5,
  9:5
}
STRICT_DUPLICATES = False



multiplierCount = {}
multipliers = []
for i in range(MIN_MULTIPLIER,MAX_MULTIPLIER+1):
    multiplierCount[i] = 0
    if i in WEIGHTING and WEIGHTING.get(i) >= 1:
      for j in range(WEIGHTING.get(i)):
          multipliers.append(i)
    else:
        multipliers.append(i)

#for i in multipliers:
#    print(i)
equations = []

#clearConsole()
allowDuplicates = False
multRange = MAX_MULTIPLIER-MIN_MULTIPLIER+1
normalLimit = int(math.pow(multRange,2))
strictLimit = int(math.factorial(multRange) / math.factorial((multRange-2)))
#for i in range(3,10):
    #permutations = (math.factorial(i)) / (math.factorial(i-2))
    #combinations = (math.factorial(i)) / (math.factorial(i-2) * math.factorial(2))
    #print(str(i) + ":\t^2: " + str(math.pow(i,2)) + "\tP: " + str(permutations) + "\tC: " + str(combinations))
if STRICT_DUPLICATES == False and normalLimit < NUM_FACTS:
  print("WARNING: Num range too small (max: " + str(normalLimit) + "), duplicates will exist.")
  allowDuplicates = True
elif STRICT_DUPLICATES == True and strictLimit < NUM_FACTS:
  print("WARNING: Num range too small (max: " + str(strictLimit) + "), duplicates will exist.")
  allowDuplicates = True

for i in range(NUM_FACTS):
  mult1 = -1
  mult2 = -1
  while True:
    mult1 = multipliers[random.randint(0,len(multipliers)-1)]
    while True:
      if mult1 in WEIGHTING and WEIGHTING.get(mult1) < 0:
        if random.randint(0,abs(WEIGHTING.get(mult1))) != abs(WEIGHTING.get(mult1)):
          mult1 = multipliers[random.randint(0,len(multipliers)-1)]
        else:
          break
      else:
        break
    mult2 = multipliers[random.randint(0,len(multipliers)-1)]
    while True:
      if mult2 in WEIGHTING and WEIGHTING.get(mult2) < 0:
        if random.randint(0,abs(WEIGHTING.get(mult2))) != abs(WEIGHTING.get(mult2)):
          mult2 = multipliers[random.randint(0,len(multipliers)-1)]
        else:
          break
      else:
        break
    if allowDuplicates == True:
      equations.append((mult1,mult2))
      break
    elif STRICT_DUPLICATES == False and not (mult1,mult2) in equations:
      equations.append((mult1,mult2))
      break
    elif STRICT_DUPLICATES == True and not (mult1,mult2) in equations and not(mult2,mult1) in equations:
      equations.append((mult1,mult2))
      break

  multiplierCount[mult1] = multiplierCount.get(mult1)+1
  multiplierCount[mult2] = multiplierCount.get(mult2)+1

for i in multiplierCount:
  print(str(i) + ": " + str(multiplierCount.get(i)))

questionNum = 1
for e in equations:
  print(str(questionNum) + ")\t" + str(e[0]) + "\tX\t" + str(e[1]) + "\t=")
  questionNum += 1