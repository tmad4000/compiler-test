
import re
S= """ 
    static int main(int argc, char argv) {
        int i = 1;
        return 2*i;
    }
"""

def do(s):
    splitInput = re.split(r'(\W)',s)
    splitInput = [m for m in splitInput if (m!= "" and m!=" " and m!="\n")]

    state="START"

    stateGraph={
        "START": ["MODIFIER", ";","RETURN_TYPE"],
        "MODIFIER": ["RETURN_TYPE"],
        "RETURN_TYPE": None
    }

    keywords={"static":"MODIFIER", "int":"RETURN_TYPE", "void":"RETURN_TYPE"}

    for i,k in enumerate(splitInput):
        if(k in keywords):

            newState=keywords[k]
            if stateGraph[state] != None and not newState in stateGraph[state]:
                print "Err", state, newState

            splitInput[i]=(k, newState)
            state=newState
            

    print(splitInput)



do(S)
