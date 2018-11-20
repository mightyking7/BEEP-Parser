
def declareVar(tokenM, varTypeD, varValueD):
    varType = tokenM.group(1)

    varName = tokenM.group(2).upper()

    varValue = tokenM.group(3)

    varTypeD[varName] = varType

    varValueD[varName] = varValue

def printVariables:

def printLabels:
    
