import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a, b):
        c = int(a) + int(b)
        print(c)
        return(True,c)