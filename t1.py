
import re
S= """ 
    (times 2 3)
    (plus 2 3)
    (setq x 4)
    (for (setq i 0) (lt i 10) (setqi plus i 1)))

    static int main(int argc, char argv) {
        int i = 1;
        return 2*i;
    }
"""

def do(s):
    splitInput = re.split(r'(\W)',s)
    splitInput = [m for m in splitInput if (m!= "" and m!=" " and m!="\n")]

    state="START"

    parseTree={f:"START", args:S}

    stateGraph={
        "START": ["EXPRESSION","MODIFIER", ";","RETURN_TYPE"],
        "MODIFIER": ["RETURN_TYPE"],
        "RETURN_TYPE": None
    }

    keywords={"static":"MODIFIER", "int":"RETURN_TYPE", "void":"RETURN_TYPE"}

    for i,token in enumerate(splitInput):

        if state=="START":
            if token=="(":
                parseTree=[]
                nextState="FUNC"
            else:
                print "ERR"

        elif state=="FUNC":
            if token in ["times","plus"]:
                addFunc(token)
                nextState="ARG"
            else:
                print "ERR"

        elif state=="ARG":
            if token=="times":
                nextState="ARG"
            elif token=="plus":
                nextState="ARG"
            else:
                print "ERR"

        if token=="(":
            state="("
        
        
        possibleNextStates=stateGraph[state]
        
        if(token in keywords):
            newState=keywords[token]
            if possibleNextStates != None and not newState in possibleNextStates:
                print "Err", state, newState

            splitInput[i]=(token, newState)
            state=newState
            

    print(splitInput)



do(S)
