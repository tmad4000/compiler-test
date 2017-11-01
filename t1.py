
import re
S= """ 
    (times 2 3)
"""

    # (plus 2 3)
    # (setq x 4)
    # (for (setq i 0) (lt i 10) (setqi plus i 1)))

    # static int main(int argc, char argv) {
    #     int i = 1;
    #     return 2*i;
    # }

def isPrim(expr):
    return re.match(r"[0-9]+$", expr) != None

# def parseRec(expr):
#     if(isPrim(expr)):
#         return expr
#     else:
#         return (func, map(lamba a: parseRec(a), args))


# def do(s):
#     splitInput = re.split(r'(\W)',s)
#     splitInput = [m for m in splitInput if (m!= "" and m!=" " and m!="\n")]

#     state="START"

#     parseTree={f:"START", args:S}

#     # stateGraph={
#     #     "START": ["EXPRESSION","MODIFIER", ";","RETURN_TYPE"],
#     #     "MODIFIER": ["RETURN_TYPE"],
#     #     "RETURN_TYPE": None
#     # }

#     # keywords={"static":"MODIFIER", "int":"RETURN_TYPE", "void":"RETURN_TYPE"}

#     def addFunc(f):
#         parseTreeCurrNode.func=f

#     def addArg(a):
#         parseTreeCurrNode.args.append(a)


#     for i,token in enumerate(splitInput):

#         if state=="START":
#             if token=="(":
#                 parseTree=[]
#                 nextState="FUNC"
#             else:
#                 print "ERR", state

#         elif state=="FUNC":
#             if token in ["times","plus"]:
#                 addFunc(token)
#                 nextState="ARG"
#             else:
#                 print "ERR", state

#         elif state=="ARG":
#             if token==")":
#                 nextState="DONE"
#             else:
#                 addArg(token)
#                 nextState="ARG"
#         elif state=="DONE":
#             pass
#         else:
#             print "ERR", state


#     print(splitInput)



# do(S)
