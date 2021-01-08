import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self):
        c = 3 + 4
        print(c)
        return(True,c)