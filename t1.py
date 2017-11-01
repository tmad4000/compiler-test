
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

    for i,token in enumerate(splitInput):
        nextState=stateGraph[state]
        
        if(token in keywords):
            newState=keywords[token]
            if nextState != None and not newState in nextState:
                print "Err", state, newState

            splitInput[i]=(token, newState)
            state=newState
            

    print(splitInput)



do(S)
