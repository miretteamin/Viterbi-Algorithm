def viterbi_algorithm(states, obsSeq, pi, transMat, emitMat):
    nodesValues = [{}]
    # Adding first states with first observation
    for st in states:
        nodesValues[0][st] = {'prob': pi[st] * emitMat[st][obsSeq[0]], 'prev': None}

    # Calculating probabilities and taking the max one
    for i in range(1, len(obsSeq)):
        nodesValues.append({})
        for st in states:
            maxProb = nodesValues[i - 1][states[0]]["prob"] * transMat[states[0]][st] * emitMat[st][obsSeq[i]]
            maxPrev = states[0]
            for prev in states[1:]:
                temp = nodesValues[i - 1][prev]["prob"] * transMat[prev][st] * emitMat[st][obsSeq[i]]
                if temp > maxProb:
                    maxProb = temp
                    maxPrev = prev

            nodesValues[i][st] = {"prob": maxProb, "prev": maxPrev}
 
    
    res = []
    lastState = None
    maxProb = 0.0

    # Backtracking
    for i in range(len(nodesValues) - 1, -1, -1):
        # Choosing the node that has the highest to probability to begin backtracking from
        if(i == len(nodesValues) - 1):
            for st, p in nodesValues[i].items():
                if p["prob"] > maxProb:
                    maxProb = p["prob"]
                    lastState = st
            res.append(lastState)
            previousState = lastState
        else:
            # Append before the first element (in index 0) As it's backtracking
            res.insert(0, nodesValues[i + 1][previousState]["prev"])
            previousState = nodesValues[i + 1][previousState]["prev"]

    return {'sequence': ' '.join(res), 'prob': maxProb}


# Input
print("Enter States\nEnter the entries in a single line (separated by space): ")
states = input().split()

print("Pi list\nEnter the entries in a single line (separated by space) with the same order you entered the states with: ")
entries = list(map(float, input().split()))
pi = dict([(st, entries[states.index(st)]) for st in states])

print("Emission characterization list\nEnter the entries in a single line (separated by space): ")
emit = input().split()

print("Enter Transition Matrix (Matrix A)\nEnter the entries in a single line (separated by space) (Enter the values from left to right all over the matrix): ")
entries = list(map(float, input().split()))
matrixA = {}
for st in states:
    matrixA[st] = dict(zip(states, entries))
    entries = entries[len(states):] # Removing taken values from entries
 
print("Enter Emission Matrix (Matrix B)\nEnter the entries in a single line (separated by space) (Enter the values from left to right all over the matrix): ")
entries = list(map(float, input().split()))
matrixB = {}
for st in states:
    matrixB[st] = dict(zip(emit, entries))
    entries = entries[len(emit):] # Removing taken values from entries

print("Enter the sequence of observations in a single line (separated by space): ")
obsSeq = input().split()


# Showing Problem inputs
print("\nProblem Input\n----------------------","\nStates: ", states, "\nPi: ", pi, "\nTransition Matrix: ", matrixA, "\nEmission Matrix: ", matrixB)


# Output 
res = viterbi_algorithm(states, obsSeq, pi, matrixA, matrixB)

print("Highest probability goes to this sequence:", res['sequence'], "\nWith probability = ", res['prob'])