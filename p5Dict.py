
def declareVar(tokenM, varTypeD, varValueD):

    varType = tokenM.group(1).upper()

    varName = tokenM.group(2).upper()

    varValue = tokenM.group(3)

    varTypeD[varName] = varType

    varValueD[varName] = varValue

def printVariables(varTypeD, varValueD):
    
    print("Variables:")

    print("%12s %8s %8s"%("Variable", "Type", "Value"))

    for name in sorted(varTypeD):
        print("    %-10s   %-8s %-8s"%(name, varTypeD[name], varValueD[name]) )


def printLabels(labelD):

    print("Labels:")

    print("%9s %16s" %("Label", "Statement"))

    for name in sorted(labelD):
        print("    %-10s   %-8s" %(name, labelD[name]))
    
